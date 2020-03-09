import nltk
from nltk import load_parser

fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')
print(fs1)

fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
print(fs2)

cp = load_parser('grammars/book_grammars/sql10.fcfg')
query = 'What cities are located in China'
tokens = query.split()
for tree in cp.parse(tokens):
  print(tree)