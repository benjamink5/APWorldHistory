#!/usr/bin/env python3
"""Convert Markdown files to PDF: pandoc -> HTML (+ mermaid.js) -> WebKit print.

usage: python3 -I md2pdf.py [options] FILE.md [FILE.md ...]

  -o, --out PATH     output PDF (one input) or output folder (several inputs).
                     Default: <repo>/Output/, mirroring the input's path in the repo
                     (Unit1/Notes/X.md -> Output/Unit1/Notes/X.pdf). Output/ is gitignored.
  --a4               A4 paper (default: US Letter).
  --no-answers       leave flashcard <details> answers closed (questions only).
  --keep-h3 / --no-keep-h3
                     keep every "### ..." block on one page. Default: on for test
                     files (name contains MCQ, Test, DBQ, Practice, Questions,
                     AnswerKey, Explanations), off otherwise.
  --html             also keep the intermediate HTML next to the PDF (for debugging).

Needs pandoc and the Xcode command line tools (swiftc). mermaid.min.js is not
downloaded (the network is blocked); a local copy is searched for, or set MERMAID_JS.
"""
import argparse, glob, hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]  # <repo>/.claude/skills/md-to-pdf/scripts
OUTPUT = REPO / "Output"
CACHE = pathlib.Path.home() / "Library" / "Caches" / "md-to-pdf"
TEST_NAME = re.compile(r"MCQ|Test|DBQ|Practice|Questions|AnswerKey|Explanations", re.I)

MERMAID_CANDIDATES = [
    os.environ.get("MERMAID_JS", ""),
    str(HERE / "vendor" / "mermaid.min.js"),
    str(pathlib.Path.home() / ".claude/plugins/marketplaces/keynote-mermaid/lib/mermaid.min.js"),
    *sorted(glob.glob(str(pathlib.Path.home() / ".npm/_npx/*/node_modules/mermaid/dist/mermaid.min.js"))),
    "/Applications/Markdown Peek.app/Contents/Resources/MarkdownRendering_MarkdownRendering.bundle/Contents/Resources/mermaid.min.js",
    "/Applications/Enchanté.app/Contents/Resources/mermaid.min.js",
]

HEADER = """<script src="mermaid.min.js"></script>
<script>
window.__mermaidErrors = [];
document.addEventListener("DOMContentLoaded", async () => {
  if (%(open)s) document.querySelectorAll("details").forEach(d => d.open = true);
  const nodes = [...document.querySelectorAll("pre.mermaid")];
  if (nodes.length && window.mermaid) {
    mermaid.initialize({ startOnLoad: false, theme: "neutral", securityLevel: "loose",
                         flowchart: { useMaxWidth: true }, gantt: { useMaxWidth: true } });
    for (let i = 0; i < nodes.length; i++) {
      const el = nodes[i], src = el.textContent;
      try { await mermaid.run({ nodes: [el] }); }
      catch (e) {
        window.__mermaidErrors.push({ index: i + 1, firstLine: src.trim().split("\\n")[0],
                                      error: String(e && e.message || e).split("\\n").slice(0, 3).join(" ") });
        el.classList.add("failed");
        el.textContent = "Mermaid diagram " + (i + 1) + " could not be drawn:\\n\\n" + src;
      }
    }
  } else if (nodes.length) {
    window.__mermaidErrors.push({ index: 0, firstLine: "", error: "mermaid.js not loaded" });
  }
  window.__renderDone = true;
});
</script>
"""


def find_mermaid():
    for c in MERMAID_CANDIDATES:
        if c and os.path.isfile(c):
            return c
    return None


def html2pdf_binary():
    src = HERE / "html2pdf.swift"
    digest = hashlib.sha1(src.read_bytes()).hexdigest()[:12]
    exe = CACHE / f"html2pdf-{digest}"
    if not exe.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(["swiftc", "-O", str(src), "-o", str(exe)], capture_output=True, text=True)
        if r.returncode:
            sys.exit("swiftc failed:\n" + r.stderr)
    return exe


def convert(md, pdf, a, exe, mermaid_js):
    keep_h3 = a.keep_h3 if a.keep_h3 is not None else bool(TEST_NAME.search(md.name))
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copy(HERE / "print.css", tmp / "print.css")
        if mermaid_js:
            shutil.copy(mermaid_js, tmp / "mermaid.min.js")
        (tmp / "header.html").write_text(HEADER % {"open": "false" if a.no_answers else "true"}, encoding="utf-8")
        html = tmp / "doc.html"
        cmd = ["pandoc", str(md), "-f", "markdown+pipe_tables+task_lists+raw_html+lists_without_preceding_blankline+autolink_bare_uris-blank_before_header-fancy_lists-tex_math_dollars-citations-implicit_figures-subscript-superscript",
               "-t", "html5", "--standalone", "--css", "print.css", "-H", str(tmp / "header.html"),
               "--lua-filter", str(HERE / "filter.lua"), "-M", f"pagetitle={md.stem}", "-o", str(html)]
        if keep_h3:
            cmd += ["-M", "keep_h3=true"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            return {"ok": False, "error": "pandoc: " + r.stderr.strip()}
        pdf.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run([str(exe), str(html), str(pdf), "a4" if a.a4 else "letter"], capture_output=True, text=True)
        if a.html:
            shutil.copy(html, pdf.with_suffix(".html"))
        try:
            return json.loads(r.stdout.strip().splitlines()[-1])
        except (IndexError, json.JSONDecodeError):
            return {"ok": False, "error": (r.stdout + r.stderr).strip() or f"html2pdf exit {r.returncode}"}


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("files", nargs="+", type=pathlib.Path)
    p.add_argument("-o", "--out", type=pathlib.Path)
    p.add_argument("--a4", action="store_true")
    p.add_argument("--no-answers", action="store_true")
    p.add_argument("--keep-h3", dest="keep_h3", action="store_true", default=None)
    p.add_argument("--no-keep-h3", dest="keep_h3", action="store_false")
    p.add_argument("--html", action="store_true")
    a = p.parse_args()

    if not shutil.which("pandoc"):
        sys.exit("pandoc not found (brew install pandoc)")
    mermaid_js = find_mermaid()
    exe = html2pdf_binary()
    failed = 0
    for md in a.files:
        md = md.resolve()
        if not md.is_file():
            print(f"✗ {md}: not found"); failed += 1; continue
        if a.out and len(a.files) == 1 and a.out.suffix.lower() == ".pdf":
            pdf = a.out.resolve()
        elif a.out:
            pdf = a.out.resolve() / (md.stem + ".pdf")
        else:
            try:
                rel = md.relative_to(REPO)
            except ValueError:  # file outside the repo
                rel = pathlib.Path(md.name)
            pdf = OUTPUT / rel.with_suffix(".pdf")
        res = convert(md, pdf, a, exe, mermaid_js)
        if not res.get("ok"):
            print(f"✗ {md.name}: {res.get('error')}"); failed += 1; continue
        errs = res.get("mermaidErrors", [])
        print(f"✓ {pdf}  ({res['pages']} pages{', %d mermaid error(s)' % len(errs) if errs else ''})")
        for e in errs:
            print(f"    mermaid #{e['index']} [{e['firstLine']}]: {e['error']}")
    if mermaid_js is None:
        print("note: mermaid.min.js not found; diagrams were left as text. Set MERMAID_JS.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
