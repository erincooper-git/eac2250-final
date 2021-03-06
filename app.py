#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:32:58 2020

@author: CooplaKhann
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static routec
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/classes")
def classes():
    return render_template('link.html')

@app.route("/moosic")
def jams():
    return render_template('1006.html')
#start the server
if __name__ == "__main__":
    app.run()