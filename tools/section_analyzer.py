# -*- coding: utf-8 -*-
import markdown
import codecs

input_file = codecs.open("in.md", mode="r", encoding="utf8")
md = markdown.Markdown(extensions=['sectionparser'])

output_file = codecs.open("out.html", "w", encoding="utf8")
output_file.write("""<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>"""+md.convert(input_file.read())+"</body></html>")


