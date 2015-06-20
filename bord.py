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
import re
import markdown
from jinja2 import FileSystemLoader, Environment

CWD = os.getcwd()
OUTPUT_DIR = 'output'
CONTENT_DIR = 'content'
md = markdown.Markdown()

CONTENT_DIR = os.path.join(CWD, CONTENT_DIR)

# site = [1, 2, 3, 4, 5]

try:
    os.makedirs(os.path.join(CWD, OUTPUT_DIR))
except OSError as err:
    print ('Error while creating directory', OUTPUT_DIR)
    print ('[', err.errno, ']', err.filename, ':', err.strerror)

for inputFile in os.listdir(CONTENT_DIR):
    inputFile = os.path.join(CONTENT_DIR, inputFile)
    outputFile = re.sub('\.md$', '.html', os.path.basename(inputFile)) 
    outputFile = os.path.join(CWD, OUTPUT_DIR, outputFile)
    try:
        f = open(inputFile, 'r', encoding='utf-8')
    except IOError as e:
        print ('Error while opening', inputFile)
        print ('[', err.errno, ']', err.filename, ':', err.strerror)
    html = md.convert(f.read())
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("template.html")
    html = template.render(
            content=html)
    f.close()
    try:
        f = open(outputFile, 'w', encoding='utf-8')
    except IOError as r:
        print (e.strerror)
    f.write(html)
    f.close()
    md.reset()
