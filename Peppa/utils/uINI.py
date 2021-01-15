from configparser import ConfigParser
import os

class uINI():
    DefaultPath:str=None
    def __init__(self, path: str = None):
        self.basepath=os.path.dirname(os.getcwd())
        if path:
            uINI.DefaultPath = os.path.join(self.basepath,path)
        else:
            uINI.DefaultPath = os.path.join(self.basepath,"config.ini")

    def getSection(self, key: str, item: str):
        rc = ConfigParser()
        rc.read(uINI.DefaultPath,encoding='utf-8')
        return rc[key][item]
    def has_Section(self,secton):
        rc = ConfigParser()
        rc.read(uINI.DefaultPath,encoding='utf-8')
        return rc.has_section(secton)
    def setSection(self,secton, option, value=None):
        rc = ConfigParser()
        rc.read(uINI.DefaultPath,encoding='utf-8')
        if  rc.has_section(secton) is not True:
            rc.add_section(secton)
        rc.set(secton, option, value)
        rc.write(open(uINI.DefaultPath, 'w', encoding='utf-8'))

#    config.add_section('login') # 首先添加一个新的section
#config.set('login','username','admin')  # 写入数据
#config.set('login','password','123456') # 写入数据




#    value = config['select']['url']
#print('第一种方法读取到的值：',value)

## 第二种读取ini文件方式，通过get方法
#value = config.get('select','url')
#print('第二种方法读取到的值：',value)


