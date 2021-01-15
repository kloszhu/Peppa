
# !/usr/bin/python
# -*- coding: UTF-8 -*-

#from sqlalchemy import *
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm import Session
#from sqlalchemy.ext.declarative import declarative_base

#from entity import *
#from utils.SSH import *
#from dao.persister import *

#from dao.dao import *

#persister = Persister()
#persister.open()
#query = persister.query(w_node)
#nodes = query.filter(w_node.master==False).all()

#print len(nodes)

from utils.database.DataAccess import DataAccess
dao = DataAccess()
dao.open()

rows = dao.queryList("select * from person")
for row in rows :
    print (row[0],row[1],row[2],row[3],row[4])

dao.close()
#persister.close()