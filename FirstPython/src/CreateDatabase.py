'''
Created on Aug 22, 2021

@author: manoj
'''
import sqlite3, csv
import logging
import re

def init_db():
    conn = None;
    try:
        # connect the database
        conn = sqlite3.connect("SnappyRecruitment");
        logging.info("successfully connected the database")
        conn.row_factory = dict_factory
        cur = conn.cursor();
        #create table 
        cur.execute("CREATE TABLE IF NOT EXISTS companies (id  Integer PRIMARY KEY, 'fakeCompanyName' Text NOT NULL, description Text NOT NULL, tagline Text NOT NULL,'companyEmail' Text NOT NULL,'businessNumber' Integer NOT NULL, Restricted Text NOT NULL);")
        logging.info("successfully connected the table")
        
        #load the csv file and iterate it and load in to variable for insertation.
        with open('faux_id_fake_companies.csv','r') as fin: 
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['id'], i['fake-company-name']
              ,i['description'], i['tagline']
              ,i['company-email'],re.sub('[^0-9a-zA-Z]+', '', i['business number'])
              ,i['Restricted']) for i in dr]
            
        
        #insert the records to table
        cur.executemany("INSERT OR REPLACE INTO companies VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
        #cur.execute("UPDATE companies SET business-number = REPLACE(business number,'-','')")
        cur.execute("SELECT * FROM companies");

        result = cur.fetchall()
    
        logging.info("number of records " + str(len(result)))
        conn.commit()
        
    except Exception as e:
        logging.exception("Cannot connect or create database due to following exception ")
        logging.exception(e)
    
    finally:
        cur.close()
        conn.close()
        
        
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
        


