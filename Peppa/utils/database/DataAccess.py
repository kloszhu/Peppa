import pymysql
import pymysql.cursors
from utils.database.configuration import dbConfig as CF



class DataAccess():
    conn = None
    cursor = None
    isClosed = True
    configuration=CF()
    #def __init__(self):
    #    print(self.configuration)

    #def open(self,host=self.configuration.host,port=self.configuration.port,db=self.configuration.db,user=self.configuration.user,pwd=self.configuration.pwd) :
        
    #    self.conn = pymysql.connect(host=host,port=port,db=db,user=user,passwd=pwd,charset="utf8")
    #    self.cursor = self.conn.cursor()
    #    self.isClosed = False
    def open(self) :
        print(self.configuration.host)
        self.conn = pymysql.connect(host=self.configuration.host,port=int(self.configuration.port),db=self.configuration.db,user=self.configuration.user,passwd=self.configuration.pwd,charset="utf8")
        self.cursor = self.conn.cursor()
        self.isClosed = False

    def execute(self,cmd) :
        if self.isClosed :
            raise Exception("db is not opened!")
        ret = self.cursor.execute(cmd)
        return ret

    def queryList(self,cmd) :
        if self.isClosed :
            raise Exception("db is not opened!")

        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()

        return rows


    def commit(self):
        self.conn.commit()
    
    def rolback(self):
        self.conn.rolback()

    def close(self) :
        if self.isClosed :
            pass;
        
        self.conn.close();
        self.isClosed=True;


dao=DataAccess()