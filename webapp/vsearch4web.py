#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:12:58 2020

@author: kanthi
"""

from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)

# =============================================================================
# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')
# 
# =============================================================================

def log_to_db(req: 'flask_request', res:str) -> None:
    '''this method writes request, response to database table'''
    phrase = req.form['phrase']
    letters = req.form['letters']
    
    dbconfig = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB'}
    conn = mysql.connector.connect(**dbconfig)
    
    _SQL = """insert into log (phrase, letters, ip, browser_string, results) 
            values (%s, %s, %s, %s, %s)""" 
    
    cursor = conn.cursor()
    cursor.execute(_SQL,(phrase, letters, str(req.remote_addr), 
                         str(req.user_agent), str(res)))
    conn.commit()
    conn.close()
        
def log_request(req: 'flask_request', res:str) -> None:
    '''this method writes request, response to log file'''
    with open('vsearch.log', 'a') as logfile:
        print(req.form, req.remote_addr, req.user_agent, res, file=logfile, sep='|')

# =============================================================================
# @app.route('/viewlog')
# def view_the_log() -> str:
#     '''this method displays the log file'''
#     with open('vsearch.log') as logfile:
#         contents = []
#         for line in logfile:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     return str(contents)
# =============================================================================

@app.route('/viewlog')
def view_the_log() -> 'html':
    '''this method displays the log file'''
    _SQL = """select * from log"""
    dbconfig = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    cursor.execute(_SQL)
    res =  cursor.fetchall()
    conn.commit()
    conn.close()
    return str(res)
        
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    '''this method invokes search function and calls results template'''
    title = 'Here are your results'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    #log_request(request, results)
    log_to_db(request, results)
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