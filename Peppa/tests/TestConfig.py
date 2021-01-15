from utils import INI
ini=INI
#ini.setSection(secton="database",option= "username",value= "admin")
#ini.setSection("database", "password", "admin1234")
INI.setSection("database","host",value="121.4.203.2")
INI.setSection("database","port",value="3306")
INI.setSection("database","user",value="admin")
INI.setSection("database","pwd",value="admin1234")
INI.setSection("database","db",value="peppa")
from utils.database import configuration
conf=configuration.configuration
print(conf.host)
print(conf.port)
print(conf.pwd)
print(conf.user)
print(conf.db)

from utils.database.DataAccess import dao

dao.open()

rows = dao.queryList("select * from person")
for row in rows :
    print (row[0],row[1],row[2],row[3])

dao.close()