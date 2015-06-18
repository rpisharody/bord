#!/usr/bin/python3

""" 
    bord - The Board for your website

    bord is a static site generator written in Python 3.
    There are many static site generators like bord. 
    This one is mine.

    Written by Rahul Pisharody.
    MIT Licence

"""

""" 
    A static site generator should:
    (1) Read Files
    (2) Convert files (markdown etc.) to HTML
    (3) Run the templating engine (Jinja2 ?)
    (4) Write the output
    (5) Deploy

"""

import os
import io
import re
import markdown
import jinja2

CWD = os.getcwd()
md = markdown.Markdown()

try:
    os.makedirs('output')
except OSError as err:
    print ('Error: ', err)

for file in os.listdir('content'):
    fullPath = os.path.join(CWD, 'content', file)
    outputName = re.sub('\.md$', '.html', file)
    outputPath = os.path.join(CWD, 'output', outputName)
    md.convertFile(fullPath, outputPath)
    md.reset()
