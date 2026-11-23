// html2pdf: paginated HTML -> PDF using WebKit's own print layout.
// usage: html2pdf in.html out.pdf [letter|a4]
// Waits until the page sets window.__renderDone = true (mermaid finished), then prints.
// Prints one JSON line: {"ok":true,"pages":N,"mermaidErrors":[...]}
import AppKit
import PDFKit
import WebKit

let args = CommandLine.arguments
guard args.count >= 3 else { print("usage: html2pdf in.html out.pdf [letter|a4]"); exit(2) }
let inURL = URL(fileURLWithPath: args[1])
let outURL = URL(fileURLWithPath: args[2])
let paper = (args.count > 3 && args[3].lowercased() == "a4") ? NSSize(width: 595, height: 842) : NSSize(width: 612, height: 792)
let margin: (top: CGFloat, side: CGFloat) = (46, 50)

func fail(_ msg: String) -> Never {
    let data = try! JSONSerialization.data(withJSONObject: ["ok": false, "error": msg])
    print(String(data: data, encoding: .utf8)!)
    exit(1)
}

final class Job: NSObject, WKNavigationDelegate {
    let web = WKWebView(frame: NSRect(origin: .zero, size: paper))
    let window = NSWindow(contentRect: NSRect(origin: .zero, size: paper), styleMask: [.borderless], backing: .buffered, defer: false)
    var mermaidErrors: [Any] = []
    var polls = 0

    func start() {
        window.contentView = web
        web.navigationDelegate = self
        web.loadFileURL(inURL, allowingReadAccessTo: inURL.deletingLastPathComponent())
    }
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) { poll() }
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { fail("load failed: \(error)") }
    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { fail("load failed: \(error)") }

    func poll() {
        web.evaluateJavaScript("window.__renderDone === true ? JSON.stringify(window.__mermaidErrors || []) : null") { result, _ in
            if let json = result as? String {
                self.mermaidErrors = (try? JSONSerialization.jsonObject(with: Data(json.utf8))) as? [Any] ?? []
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) { self.printIt() }
            } else {
                self.polls += 1
                if self.polls > 300 { fail("timed out waiting for diagrams to render") }
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) { self.poll() }
            }
        }
    }

    func printIt() {
        let info = NSPrintInfo()
        info.paperSize = paper
        info.topMargin = margin.top; info.bottomMargin = margin.top
        info.leftMargin = margin.side; info.rightMargin = margin.side
        info.horizontalPagination = .fit; info.verticalPagination = .automatic
        info.isHorizontallyCentered = false; info.isVerticallyCentered = false
        info.jobDisposition = .save
        info.dictionary()[NSPrintInfo.AttributeKey.jobSavingURL] = outURL
        let op = web.printOperation(with: info)
        op.showsPrintPanel = false; op.showsProgressPanel = false
        op.view?.frame = NSRect(x: 0, y: 0, width: paper.width - 2 * margin.side, height: paper.height)
        op.runModal(for: window, delegate: self, didRun: #selector(done(_:success:context:)), contextInfo: nil)
    }

    @objc func done(_ op: NSPrintOperation, success: Bool, context: UnsafeMutableRawPointer?) {
        guard success, let doc = PDFDocument(url: outURL) else { fail("print failed") }
        let report: [String: Any] = ["ok": true, "pages": doc.pageCount, "mermaidErrors": mermaidErrors]
        let data = try! JSONSerialization.data(withJSONObject: report)
        print(String(data: data, encoding: .utf8)!)
        exit(0)
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.prohibited)
let job = Job()
job.start()
DispatchQueue.main.asyncAfter(deadline: .now() + 90) { fail("timeout") }
app.run()
