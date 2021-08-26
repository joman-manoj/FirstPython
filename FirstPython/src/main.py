'''
Created on Aug 22, 2021

@author: joman
'''
#import api;

#get companies
from app import app
from flask.templating import render_template
from CreateDatabase import init_db
from apiCalls import getCompanies, getCompany
import flask, sqlite3
from flask import request, jsonify
import logging

init_db();

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies/all', methods=['GET'])
def companies():
    if 'businessNumber' in request.args:
        return getCompany((request.args['businessNumber']));
    else:
        return getCompanies();



@app.route('/companies/<businessNumber>')
def company(businessNumber):
    return getCompany(businessNumber);   
    
if __name__ == '__main__':
    app.run(debug=True)

