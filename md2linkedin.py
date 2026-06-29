#!/usr/bin/env python3
"""Convert Markdown file to HTML and copy to clipboard (LinkedIn-ready)."""

import sys
import subprocess
import markdown

def main():
    if len(sys.argv) < 2:
        print("Usage: md2linkedin.py <file.md>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path) as f:
        md_text = f.read()

    html = markdown.markdown(md_text)

    html_doc = f"""<html><body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.5;white-space:pre-wrap">{html}</body></html>"""

    swift_script = "/Users/victor/Projects/Articles/pbcopy-html.swift"
    proc = subprocess.Popen(["/usr/bin/swift", swift_script], stdin=subprocess.PIPE)
    proc.communicate(input=html_doc.encode("utf-8"))

    if proc.returncode == 0:
        print(f"✅ Copied {path} to clipboard as HTML. Paste into LinkedIn (Cmd+V).")
    else:
        print(f"❌ Error: swift script returned {proc.returncode}")
        sys.exit(1)

if __name__ == "__main__":
    main()
