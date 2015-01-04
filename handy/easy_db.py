__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is a module letting connect to databases easily.
"""

from pymongo import MongoClient
import pymysql
#import psycopg2





def easy_mysql(cfg_dict, encoding='utf8'):
    con = pymysql.connect(host = cfg_dict['host'], user = cfg_dict['usr'], passwd = cfg_dict['pwd'], db = cfg_dict['db'], charset = encoding)
    cur = con.cursor()
    return cur
    
    
    
    
def easy_mongo(cfg_dict = "undefined", encoding='utf8', port = 27017, host = "undefined", db="undefined"):
    if cfg_dict != "undefined":
        client = MongoClient(host = cfg_dict['host'], port = port)
        db = client[cfg_dict['db']]
    elif host != "undefined" and db != "undefined":
        client = MongoClient(host = host, port = port)
        db = client[db]
    return db
    
    
    
 
def easy_postgres(cfg_dict):
    con = psycopg2.connect("dbname=%s user=%s host=%s password=%s" % (cfg_dict['db'], cfg_dict['usr'], cfg_dict['host'], cfg_dict['pwd']))
    cur = con.cursor()
    return cur






if __name__ == "__main__":
    cfg_dict = dict(host='lynn.cj4f4oszguhk.ap-northeast-1.rds.amazonaws.com', usr='root', pwd='hqam30018', 
                    db='KOREANWAVE')
    
    print("\n=========== this is easy_mysql tutorial ===========")
    print("creating connection to mysql...")
    cur = easy_mysql(cfg_dict)          #default encoding='utf8'
    
    print("fetching table list...")
    cur.execute('SHOW TABLES;')
    for t in cur:
        print(t[0])         #return value type is tuple
    cur.close()
    
    
    print("\n=========== this is easy_mongo tutorial ===========")
    print("creating connection to mongodb...")
    db = easy_mongo(host="lynn.yonsei.ac.kr", db="test")
    
    print("fetching collection list...")
    cols = db.collection_names()        #fetch collection names in the db
    for c in cols:
        print(c)
    col = db[cols[1]]
    
    print("fetching document list...")
    docs = col.find()       #fetch all docs in the collection
    for d in docs:
        print(d)
        
        
        
        
