'''
Created on Aug 23, 2021

@author: joman
'''

import flask, sqlite3
from flask import request, jsonify
import logging
from pickletools import string1

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getCompanies():
    try:
        #to_filter = [];
        conn = sqlite3.connect("SnappyRecruitment");
        conn.row_factory = dict_factory
        cur = conn.cursor();
        results = cur.execute("SELECT * FROM companies").fetchall()
        resp = jsonify(results)
        resp.status_code = 200
        return resp
       
    except Exception as e:
        logging.exception(e)
    finally:
        cur.close() 
        conn.close()
        
def getCompany(businessNumber):
    try:
        conn = sqlite3.connect("SnappyRecruitment");
        conn.row_factory = dict_factory
        cursor = conn.cursor();
        query = "SELECT * FROM companies WHERE businessNumber=? AND Restricted='Yes'"
        param = int(businessNumber)  
        
        cursor.execute(query,[param])
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()