import pywhatkit
from flask import Flask
txt = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
    Its high-level built in data structures, combined with dynamic typing and dynamic binding,
    make it very attractive for Rapid Application Development,as well as for use as a scripting or glue language to connect existing components together'''
pywhatkit.text_to_handwriting(txt,'demo1.png',[255,0,0])
print('File converted and save in the same folder as the program')