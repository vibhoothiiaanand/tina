#!/usr/bin/env python

import PyPDF2
import sys
import os
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from docx import Document
from importlib import reload
import html2text

input_dir = sys.argv[1]

files = []

for i in os.listdir(input_dir):
    thefile = os.path.join(input_dir, i)
    if i.endswith('.docx'):
        document = Document(thefile)
        count = 1
        w = open(str(count) + '.txt', "a")
        
        newparatextlist = []

        for para in document.paragraphs:
            newparatextlist.append(para.text)
        string = ''.join(str(e) for e in newparatextlist)
        count = count + 1
        w.write(string)
        w.close()

    elif i.endswith('.html'):
        count = 1
        html = open(input_dir + '/' + i)
        f = html.read()
            
        w = open(str(count) + '.txt', "a")

        h_parser = html2text.HTML2Text()

        h_parser.ingnore_links = True
        h_parser.ignore_anchors = True
        h_parser.inline_links = False
        h_parser.ingnore_emphasis = True
        h_parser.ignore_links = True

        text = h_parser.handle(f)
        text = text.strip(' \t\n\r')
        text = text.replace('\\n', '')
        count = count + 1
        w.write(text)
        w.close()

    elif i.endswith('.pdf'):
        count = 1
        pdfFileObj = open(thefile,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        w = open(str(count) + '.txt', "a")

        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()
        if text != "":
            text = text
        else:
            text = textract.process(thefile, method='tesseract', language='eng')
        count = count + 1
        w.write(text)
        w.close()


f = open("bigfile.txt", "w+")
path = '/home/aniketh/devel/src/miner/extractor'
files = os.listdir(path)
for tempfile in files:
    if i.endswith('.txt'):
        f.write(tempfile.read())

