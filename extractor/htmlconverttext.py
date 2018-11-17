#!/usr/bin/env python

import sys
import html2text

h_parser = html2text.HTML2Text()

h_parser.ignore_links = True
h_parser.ignore_anchors = True
h_parser.inline_links = True


html = open(sys.argv[1])
f = html.read()
w = open("out.txt", "w")
w.write(html2text.html2text(f))
html.close()
w.close()

