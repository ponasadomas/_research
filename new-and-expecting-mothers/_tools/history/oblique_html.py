"""Small stdlib HTML tree for original forum post boundaries and pagination."""
from html.parser import HTMLParser
import re

VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
BLOCK={'p','div','br','li','ul','ol','blockquote','section','article','table','tr','td','h1','h2','h3','h4','pre'}
class Node:
 def __init__(self,tag='',attrs=None,parent=None):self.tag=tag;self.attrs=dict(attrs or []);self.parent=parent;self.children=[]
 def classes(self):return self.attrs.get('class','').split()
 def has(self,c):return c in self.classes()
 def all(self,predicate):
  for c in self.children:
   if isinstance(c,Node):
    if predicate(c):yield c
    yield from c.all(predicate)
 def text(self,skip_quotes=False):
  if self.tag in ['script','style','noscript','svg','template']:return ''
  if skip_quotes and (self.tag=='blockquote' or self.has('UserSignature')):return ''
  parts=[]
  for c in self.children:parts.append(c.text(skip_quotes) if isinstance(c,Node) else c)
  s=''.join(parts)
  return ('\n'+s+'\n') if self.tag in BLOCK else s
 def clean(self,skip_quotes=False):return re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+', '\n\n',self.text(skip_quotes))).strip()
 def first(self,predicate):return next(self.all(predicate),None)

class Tree(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.root=Node('root');self.stack=[self.root]
 def handle_starttag(self,tag,attrs):
  node=Node(tag,attrs,self.stack[-1]);self.stack[-1].children.append(node)
  if tag not in VOID:self.stack.append(node)
 def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs);self.handle_endtag(tag)
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):self.stack[-1].children.append(data)

def parse(s):
 p=Tree();p.feed(s);return p.root
