from tkinter import *
import pypyodbc
import DBC as gf
root=Tk()
root.title("XML配置工具")
mdbfilepath="E:\Projects\pypy\管线.mdb"
where='江山'
bool='false'
surtablename=[]
surfieldname=[]
pointfieldname={}
surlinefieldname=[]
surpointfieldname=[]
stdpointtablename=['JSPOINT','YSPOINT','WSPOINT','GDPOINT']
stdlinetablename=['JSLINE','YSLINE','WSLINE','GDLINE']
stdpointfieldname=['物探点号','特征点','附属物']
stdlinefieldname=['起点点号','终点点号','起点高程','终点高程','起点埋深','终点埋深']
sqltablename='select name from MSysObjects WHERE type=1 and flags=0'

def hello():
    print("试试")
def buildDBC(root):
    print("buildDBC")
    print(pointfieldname)
    allfield = gf.getallfield(root,pointfieldname)
    print(allfield)
def buildM():
    print("buildM")
menubar=Menu(root)
menufile=Menu(menubar,tearoff=0)
menufile.add_command(label='打开', command=hello)
menufile.add_separator()
menufile.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=menufile)
menuXML=Menu(menubar,tearoff=0)
menuXML.add_command(label='bulidBDC',command=buildDBC)
menuXML.add_command(label='bulidModel',command=buildM)
menubar.add_cascade(label='XML文件生成', menu=menuXML)
root.config(menu=menubar)
root.geometry('200x400')

mdbpath = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s;'%mdbfilepath

db=pypyodbc.win_connect_mdb(mdbpath)                 # 打开数据库连接
cursor = db.cursor()  # 产生cursor游标

# 获取数据库中每个表名 surtablename
cursor.execute(sqltablename) #获取每个表名，注意设置对MSysObjects表的权限
restablename = cursor.fetchall()
for i in restablename:
    surtablename.append(i[0])
# print(surtablename)
# 获取每张点表的表头 surpointfieldname
cursor.execute('select * from '+ surtablename[1] +' WHERE false')
for i in cursor.description:
    m=str(i[1])
    m=m.replace("<class '",'')
    m=m.replace("'>",'')
    pointfieldname[i[0]]=m
# print(pointfieldname)



# 获取每张线表的表头 surlinefieldname
cursor.execute('select * from '+ surtablename[0] +' WHERE false')
for i in cursor.description:
    surlinefieldname.append(i[0])
    surlinefieldname.append(i[1])
# print(surlinefieldname)
cursor.close()

root.mainloop()
print("OK")