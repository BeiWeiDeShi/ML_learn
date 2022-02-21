#!/usr/bin/python3
import os
import re
import json
from sys import argv

with open(argv[1]) as fd:
    content = fd.read()
    content = re.sub(r'\n', '', content)
    obj = json.loads(content)
    for cell in obj['cells']:
        if cell['cell_type'] == 'code':
            cell['execution_count'] = None
            cell['outputs'] = []
            if (len(cell['source']) > 0 and cell['source'][0].startswith('##keep')):
                continue
            cell['source'] = []
    print(json.dumps(obj))
