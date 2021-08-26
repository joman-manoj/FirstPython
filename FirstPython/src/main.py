'''
Created on Aug 22, 2021

@author: Manoj
'''

from app import app
from flask.templating import render_template
from CreateDatabase import init_db
from apiCalls import getCompanies, getCompany
from flask import request

#Initialize the database , Schema creation done her
init_db();

#redirect the page for search companies
@app.route('/')
def index():
    return render_template('index.html')

#search by business number otherwise get all
@app.route('/companies/all', methods=['GET'])
def companies():
    #if the request has the business number then return the exact matching records 
    #otherwise returns all the restricted companies
    if ('businessNumber' in request.args and len((request.args['businessNumber']))):  
        return getCompany((request.args['businessNumber']));
    else:
        return getCompanies(); 
    
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080,debug=True)


