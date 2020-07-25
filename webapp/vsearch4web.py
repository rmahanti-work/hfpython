#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:12:58 2020

@author: kanthi
"""

from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app = Flask(__name__)

# =============================================================================
# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')
# 
# =============================================================================

def log_request(req: 'flask_request', res:str) -> None:
    '''this method writes request, response to log file'''
    with open('vsearch.log', 'a') as logfile:
        print(req.form, req.remote_addr, req.user_agent, res, file=logfile, sep='|')

@app.route('/viewlog')
def view_the_log() -> 'html':
    '''this method displays the log file'''
    title = 'View Log'
    tabletitles = ['Form Data', 'Remote_addr', 'User_agent', 'Results']
    with open('vsearch.log') as logfile:
        contents = []
        for line in logfile:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return render_template('viewlog.html',
                the_title=title,
                the_row_titles=tabletitles,
                the_data=contents,)
        
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    '''this method invokes search function and calls results template'''
    title = 'Here are your results'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    log_request(request, results)
    return render_template('results.html',
                the_title=title,
                the_phrase=phrase,
                the_letters=letters,
                the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    '''this method renders entry form for searching letters'''
    return render_template('entry.html',the_title='Welcome to search4letters on the web')
    
if __name__ == '__main__':
    app.run(debug=True)