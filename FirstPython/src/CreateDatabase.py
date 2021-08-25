'''
Created on Aug 22, 2021

@author: joman
'''
import sqlite3, csv
import logging
import re

def init_db():
    try:
        conn = sqlite3.connect("SnappyRecruitment");
        
        conn.row_factory = dict_factory
        cur = conn.cursor();
        cur.execute("DROP TABLE companies")
        #cur.execute("DELETE FROM companies")
        #create table 
        cur.execute("CREATE TABLE IF NOT EXISTS companies (id  Integer PRIMARY KEY, 'fakeCompanyName' Text NOT NULL, description Text NOT NULL, tagline Text NOT NULL,'companyEmail' Text NOT NULL,'businessNumber' Integer NOT NULL, Restricted Text NOT NULL);")
       # cur.execute("CREATE TABLE companies ('id','fake-company-name',description,tagline,'company-email',business number,Restricted);")
        with open('faux_id_fake_companies.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['id'], i['fake-company-name']
              ,i['description'], i['tagline']
              ,i['company-email'],re.sub('[^0-9a-zA-Z]+', '', i['business number'])
              ,i['Restricted']) for i in dr]
        
        #cur.execute("INSERT INTO companies VALUES(2323,'TYRRTY','DHDDHGHG','RTRRT','HDGD','HJGJ','JHGGH');")
        # * FROM companies");
        cur.executemany("INSERT INTO companies VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
        #cur.execute("UPDATE companies SET business-number = REPLACE(business number,'-','')")
        cur.execute("SELECT * FROM companies");

        result = cur.fetchall()
    
        print(len(result))
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
        


