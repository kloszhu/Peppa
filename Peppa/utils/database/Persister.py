# !/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

import configuration

class Persister(object):
    
    session = None;
    isClosed = True;

    def open(self,host=configuration.host,port=configuration.port,db=configuration.db,user=configuration.user,pwd=configuration.pwd) :
        
        url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s' % (user,pwd,host,port,db)
        engine = create_engine(url)
        DbSession = sessionmaker(bind=engine)

        self.session = DbSession()

        self.isClosed = False

        return self.session

    def query(self,type) :
        
        query = self.session.query(type)
        return query

    def add(self,item) :
        self.session.add(item)        

    def add_all(self,items) :
        self.session.add_all(items)

    def delete(self,item) :
        self.session.delete(item)

    def commit(self) :
        self.session.commit()

    def close(self) :
        
        if self.isClosed :
            pass
        
        self.session.close()
        self.isClosed = True
