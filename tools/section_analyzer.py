# -*- coding: utf-8 -*-
import markdown
import codecs
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--output-file", dest="output_file")
parser.add_option("-i", "--input-file", dest="input_file")
(options, args) = parser.parse_args()

input_file = codecs.open(options.input_file, mode="r", encoding="utf8")
md = markdown.Markdown(extensions=['sectionparser'])

output_file = codecs.open(options.output_file, "w", encoding="utf8")
output_file.write("""<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>"""+md.convert(input_file.read())+"</body></html>")


