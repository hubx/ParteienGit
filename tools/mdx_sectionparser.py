# -*- coding: utf-8 -*-
from collections import Counter
import codecs
import re
import string

from markdown.util import etree
import markdown

class SectionProcessor(markdown.treeprocessors.Treeprocessor):
  def __init__ (self, args):
    self.args = args
    f = codecs.open('german.stopwords', 'r', "utf8")
    self.STOPWORDS = map(lambda line: line.strip(), f.readlines())

  def statistic(self, lst):
    section = ""
    for text in lst.itertext():
      section += text
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    words = filter(lambda x: regex.sub('', x.lower()) not in self.STOPWORDS, section.split())
    count = Counter(words).most_common(3)
    return u"Häufige Wörter: " + ', '.join("'"+i+"':"+str(j) for i,j in count)

  def run(self, root):
    HEADLINES = ["h1","h2","h3","h4","h5","h6","h7"]
    lasttag = "h0"
    prev = None
    section_stack = etree.Element("section")
    for child in root:
      if child.tag in HEADLINES:
        if child.tag < lasttag:
          prev.tail = self.statistic(section_stack) 
          section_stack = etree.Element("section")
        lasttag = child.tag
      else:
        section_stack.append(child)
      prev = child
    return root

class SectionExtension(markdown.Extension):
  def extendMarkdown(self, md, md_globals):
    md.treeprocessors.add('section', SectionProcessor(md), '_end')

def makeExtension(configs=None) :
  return SectionExtension(configs=configs)
