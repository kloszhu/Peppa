from utils import uINI

class dbConfig():
    host="127.0.0.1"
    port=3306
    user="root"
    pwd="admin"
    db="peppa"
    def __init__(self):
        ini=uINI()
        if ini.has_Section("database"):
            self.host=ini.getSection("database","host")
            self.port=ini.getSection("database","port")
            self.user=ini.getSection("database","user")
            self.pwd=ini.getSection("database","pwd")
            self.db=ini.getSection("database","db")

configuration=dbConfig()