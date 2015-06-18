#!/usr/bin/python3

""" 
    bord - The Board for your website

    bord is a static site generator written in Python 3.
    There are many static site generators like bord. 
    This one is mine.

    Written by Rahul Pisharody.
    MIT Licence

"""

import os
import io
import re
import markdown
import jinja2

CWD = os.getcwd()
OUTPUT_DIR = 'output'
CONTENT_DIR = 'content'
md = markdown.Markdown()

CONTENT_DIR = os.path.join(CWD, CONTENT_DIR)
OUTPUT_DIR = os.path.join(CWD, OUTPUT_DIR)

try:
    os.makedirs(OUTPUT_DIR)
except OSError as err:
    print ('Error while creating', OUTPUT_DIR)
    print ('[', err.errno, ']', err.filename, ':', err.strerror)

for inputFile in os.listdir(CONTENT_DIR):
    inputfile = os.path.join(CONTENT_DIR, inputfile)
    outputFile = re.sub('\.md$', '.html', inputFile) 
    md.convertFile(inputFile, outputFile)
    md.reset()
