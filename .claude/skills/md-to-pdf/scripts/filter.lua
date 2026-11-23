-- Pandoc Lua filter for md2pdf.
-- 1. ```mermaid code blocks become <pre class="mermaid"> so mermaid.js can draw them.
-- 2. A question paragraph ("**12.** ..." or "**Question 12**") and the option list after it
--    are wrapped in <div class="q"> so a page break never splits them.
-- 3. If the metadata flag keep_h3 is set (test files), every "### ..." block is wrapped
--    in <div class="q"> as well (Unit 4/5 tests put one question under each ### heading).

local function escape_html(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

local function trim(s) return (s:gsub("^%s+", ""):gsub("%s+$", "")) end

-- A Mermaid timeline with many events is drawn very wide, and scaling it to the page
-- makes the text unreadable. Print it as a "Year | Events" table instead.
-- Handles "title ...", "section ...", "YEAR : a : b", and continuation lines " : c".
local function timeline_table(text)
  local title, rows = nil, {}
  for line in text:gmatch("[^\n]+") do
    local l = trim(line)
    if l == "timeline" or l == "" or l:match("^%%%%") then
      -- skip
    elseif l:match("^title%s") then
      title = trim(l:sub(6))
    elseif l:match("^section%s") then
      table.insert(rows, {section = trim(l:sub(8))})
    else
      local parts = {}
      for p in (l .. ":"):gmatch("(.-):") do table.insert(parts, trim(p)) end
      local when = table.remove(parts, 1)
      if when == "" and #rows > 0 and rows[#rows].events then
        for _, e in ipairs(parts) do if e ~= "" then table.insert(rows[#rows].events, e) end end
      else
        local ev = {}
        for _, e in ipairs(parts) do if e ~= "" then table.insert(ev, e) end end
        table.insert(rows, {when = when, events = ev})
      end
    end
  end
  local h = {'<table class="timeline">'}
  if title then table.insert(h, "<caption>" .. escape_html(title) .. "</caption>") end
  for _, r in ipairs(rows) do
    if r.section then
      table.insert(h, '<tr class="section"><th colspan="2">' .. escape_html(r.section) .. "</th></tr>")
    else
      local ev = {}
      for _, e in ipairs(r.events) do table.insert(ev, escape_html(e)) end
      table.insert(h, '<tr><td class="when">' .. escape_html(r.when) .. "</td><td>" .. table.concat(ev, "<br/>") .. "</td></tr>")
    end
  end
  table.insert(h, "</table>")
  return table.concat(h, "\n")
end

function CodeBlock(cb)
  if cb.classes:includes("mermaid") then
    local first = trim(cb.text:match("^%s*([^\n]*)") or "")
    if first == "timeline" then
      return pandoc.RawBlock("html", timeline_table(cb.text))
    end
    return pandoc.RawBlock("html", '<pre class="mermaid">' .. escape_html(cb.text) .. "</pre>")
  end
end

-- Pandoc fixes column widths from the length of the |---| separator, which gives a short
-- code column (KC, Topic) the same width as a long text column. Drop the fixed widths so
-- the browser sizes columns to their content.
function Table(t)
  for i, cs in ipairs(t.colspecs) do
    t.colspecs[i] = {cs[1], pandoc.ColWidthDefault}
  end
  return t
end

local function is_question(b)
  if b.t ~= "Para" and b.t ~= "Plain" then return false end
  local first = b.content[1]
  if not first or first.t ~= "Strong" then return false end
  local txt = pandoc.utils.stringify(first)
  return txt:match("^%d+%.$") or txt:match("^Question%s+%d+") or txt:match("^Q%d+")
end

local function wrap_questions(blocks)
  local out, i = {}, 1
  while i <= #blocks do
    local b = blocks[i]
    local nxt = blocks[i + 1]
    if is_question(b) and nxt and (nxt.t == "BulletList" or nxt.t == "OrderedList") then
      table.insert(out, pandoc.Div({b, nxt}, {class = "q"}))
      i = i + 2
    else
      table.insert(out, b)
      i = i + 1
    end
  end
  return out
end

local function wrap_h3(blocks)
  local out, cur = {}, nil
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.level == 3 then
      if cur then table.insert(out, pandoc.Div(cur, {class = "q"})) end
      cur = {b}
    elseif b.t == "Header" or b.t == "HorizontalRule" then
      if cur then table.insert(out, pandoc.Div(cur, {class = "q"})); cur = nil end
      table.insert(out, b)
    elseif cur then
      table.insert(cur, b)
    else
      table.insert(out, b)
    end
  end
  if cur then table.insert(out, pandoc.Div(cur, {class = "q"})) end
  return out
end

function Pandoc(doc)
  doc = doc:walk({CodeBlock = CodeBlock, Table = Table})
  local blocks = wrap_questions(doc.blocks)
  if doc.meta.keep_h3 then blocks = wrap_h3(blocks) end
  doc.blocks = blocks
  return doc
end
