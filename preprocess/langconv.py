from copy import deepcopy
import re

try:
  import psyco
  psyco.full()
except ImportError:
  from zhtools.zh_wiki import zh2Hant, zh2Hans

import sys
py3k = sys.version_info >= (3, 0, 0)

if py3k:
  UEMPTY = ''
else:
  _zh2Hant, _zh2Hans = {}, {}
  for old, new in ((zh2Hant, _zh2Hant), (zh2Hans, _zh2Hans)):
    for k, v in old.items():
      new[k.decode('utf8')] = v.decode('utf8')
  zh2Hant = _zh2Hant
  zh2Hans = _zh2Hans
  UEMPTY = ''.decode('utf8')

(START, END, FAIL, WAIT_TAIL) = list(range(4))
(TAIL, ERROR, MATCHED_SWITCH, UNMATCHED_SWITCH, CONNECTOR) = list(range(5))