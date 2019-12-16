#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort, uniq
from WordCount import wc
from Usage import usage, err

import sys

valid_tools = {'cat' : cat,'tac' : tac,'cut' : cut,'paste' : paste,'grep': grep,'head': head,'tail' : tail, 'sort' : sort, 'uniq' : uniq, 'wc' : wc}

if len(sys.argv) < 3:
    err('Error: Too few arguments\n')
    usage()
    sys.exit(1)
else:
    tool = sys.argv[1]
    if tool in valid_tools:
        valid_tools[tool](sys.argv)
    else:
        err('Specifyed tool "' + tool + '" invalid')
        usage()

