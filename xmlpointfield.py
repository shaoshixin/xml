from xml.dom.minidom import Document
import re
import pypyodbc
import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()
mdbfilepath="E:\Projects\pypy\管线.mdb"
where=""
bool=""
surtablename=[]
pointfieldname={}
mdbpath = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s;'%mdbfilepath
db=pypyodbc.win_connect_mdb(mdbpath)                 # 打开数据库连接
cursor = db.cursor()  # 产生cursor游标

# 获取数据库中每个表名 surtablename
cursor.execute('select name from MSysObjects WHERE type=1 and flags=0') #获取每个表名，注意设置对MSysObjects表的权限
restablename = cursor.fetchall()
for i in restablename:
    surtablename.append(i[0])
# 获取每张点表的表头 surpointfieldname
cursor.execute('select * from '+ surtablename[1] +' WHERE false')
for i in cursor.description:
    m=str(i[1])
    m=m.replace("<class '",'')
    m=m.replace("'>",'')
    pointfieldname[i[0]]="T:"+m

n = []
for (k, v) in pointfieldname.items():
    n.append(k + " " + v)

pointfield={}
def go(*args):
    bool=cblbool.get()
    where=entry.get()
    pointfield["物探点号"]=re.compile(r'.T.*').sub('',cbl1.get())
    pointfield["图上点号"]=re.compile(r'.T.*').sub('',cbl2.get())
    pointfield["特征点"]=re.compile(r'.T.*').sub('',cbl3.get())
    pointfield["附属物"]=re.compile(r'.T.*').sub('',cbl4.get())
    pointfield["X坐标"]=re.compile(r'.T.*').sub('',cbl5.get())
    pointfield["Y坐标"]=re.compile(r'.T.*').sub('',cbl6.get())
    pointfield["管线性质"]=re.compile(r'.T.*').sub('',cbl7.get())
    pointfield["地面高程"]=re.compile(r'.T.*').sub('',cbl8.get())
    pointfield["井底深"]=re.compile(r'.T.*').sub('',cbl9.get())
    pointfield["井盖规格"]=re.compile(r'.T.*').sub('',cbl10.get())
    pointfield["井盖类型"]=re.compile(r'.T.*').sub('',cbl11.get())
    pointfield["井盖材质"]=re.compile(r'.T.*').sub('',cbl12.get())
    pointfield["井盖附属物代码"]=re.compile(r'.T.*').sub('',cbl13.get())
    pointfield["井室规格"]=re.compile(r'.T.*').sub('',cbl14.get())
    pointfield["井室角度"]=re.compile(r'.T.*').sub('',cbl15.get())
    pointfield["井盖照片代码"]=re.compile(r'.T.*').sub('',cbl16.get())
    pointfield["图幅号"]=re.compile(r'.T.*').sub('',cbl17.get())
    pointfield["偏心井位"]=re.compile(r'.T.*').sub('',cbl18.get())
    pointfield["所在道路"]=re.compile(r'.T.*').sub('',cbl19.get())
    pointfield["探测单位"]=re.compile(r'.T.*').sub('',cbl20.get())
    pointfield["探测时间"]=re.compile(r'.T.*').sub('',cbl21.get())
    pointfield["备注"]=re.compile(r'.T.*').sub('',cbl22.get())
    # 删除字典中值为空的元素
    m_key=list(pointfield.keys())
    for m_s in m_key:
        if pointfield[m_s]== "":
            pointfield.pop(m_s)
    print(pointfield)

    # 将self.orderDict中的信息写入本地xml文件，参数filename是xml文件名

    # 创建dom文档
    doc = Document()
    # 创建根节点
    config = doc.createElement('Config')
    # 根节点插入dom树
    doc.appendChild(config)
    scheme = doc.createElement('Scheme')
    scheme.setAttribute('Name', where + '管线成图方案')
    scheme.setAttribute('Description', where + '管线成图方案')
    scheme.setAttribute('DealHField', bool)
    config.appendChild(scheme)

    # 依次将orderDict中的每一组元素提取出来，创建对应节点并插入dom树
    # 创建节点<PointFields>
    pointfields = doc.createElement('PointFields')
    scheme.appendChild(pointfields)

    for (k,v) in pointfield.items():
        (std,sur)=(k,v)
        field = doc.createElement('Field')
        field.setAttribute('Source',sur)
        field.setAttribute('Standard', std)
        pointfields.appendChild(field)
        # 将电话插入<LineFields>中，处理同上

    # linefields = doc.createElement('LineFields')
    # scheme.appendChild(linefields)

    # 将dom对象写入本地xml文件
    f = open('BuildDBCfg.xml', 'w', encoding='utf_8_sig')
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='UTF-8')
    f.close()

btn = ttk.Button(root, text="确定", command=go)
btn.grid(row=0,column=0)

lab = tk.Label(root, text="项目名称：")
lab.grid(row=1,column=0)
entry = tk.Entry(root, textvariable=tk.StringVar())
entry.grid(row=1,column=1)

lab = tk.Label(root, text="是否处理高程")
lab.grid(row=2,column=0)
cblbool = ttk.Combobox(root, textvariable=tk.StringVar())
cblbool.grid(row=2,column=1)
cblbool['values'] = ["false","true"]
cblbool.current(0)

cbl22 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="备注")
cbl22['values'] = n
lab.grid(row=24, column=0)
cbl22.grid(row=24, column=1)

lab = tk.Label(root, text="物探点号")
lab.grid(row=3,column=0)
cbl1 = ttk.Combobox(root, textvariable=tk.StringVar())
cbl1.grid(row=3,column=1)
cbl1['values'] = n

cbl2 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="图上点号")
cbl2['values'] = n
lab.grid(row=4, column=0)
cbl2.grid(row=4, column=1)

cbl3 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="特征点")
cbl3['values'] = n
lab.grid(row=5, column=0)
cbl3.grid(row=5, column=1)

cbl4 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="附属物")
cbl4['values'] = n
lab.grid(row=6, column=0)
cbl4.grid(row=6, column=1)

cbl5 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="X坐标")
cbl5['values'] = n
lab.grid(row=7, column=0)
cbl5.grid(row=7, column=1)

cbl6 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="Y坐标")
cbl6['values'] = n
lab.grid(row=8, column=0)
cbl6.grid(row=8, column=1)

cbl7 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="管线性质")
cbl7['values'] = n
lab.grid(row=9, column=0)
cbl7.grid(row=9, column=1)

cbl8 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="地面高程")
cbl8['values'] = n
lab.grid(row=10, column=0)
cbl8.grid(row=10, column=1)

cbl9 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井底深")
cbl9['values'] = n
lab.grid(row=11, column=0)
cbl9.grid(row=11, column=1)

cbl10 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井盖规格")
cbl10['values'] = n
lab.grid(row=12, column=0)
cbl10.grid(row=12, column=1)

cbl11 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井盖类型")
cbl11['values'] = n
lab.grid(row=13, column=0)
cbl11.grid(row=13, column=1)

cbl12 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井盖材质")
cbl12['values'] = n
lab.grid(row=14, column=0)
cbl12.grid(row=14, column=1)

cbl13 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井室附属物代码")
cbl13['values'] = n
lab.grid(row=15, column=0)
cbl13.grid(row=15, column=1)

cbl14 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井室规格")
cbl14['values'] = n
lab.grid(row=16, column=0)
cbl14.grid(row=16, column=1)

cbl15 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井室角度")
cbl15['values'] = n
lab.grid(row=17, column=0)
cbl15.grid(row=17, column=1)

cbl16 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="井盖照片代码")
cbl16['values'] = n
lab.grid(row=18, column=0)
cbl16.grid(row=18, column=1)

cbl17 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="图幅号")
cbl17['values'] = n
lab.grid(row=19, column=0)
cbl17.grid(row=19, column=1)

cbl18 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="偏心井位")
cbl18['values'] = n
lab.grid(row=20, column=0)
cbl18.grid(row=20, column=1)

cbl19 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="所在道路")
cbl19['values'] = n
lab.grid(row=21, column=0)
cbl19.grid(row=21, column=1)

cbl20 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="探测单位")
cbl20['values'] = n
lab.grid(row=22, column=0)
cbl20.grid(row=22, column=1)

cbl21 = ttk.Combobox(root, textvariable=tk.StringVar())
lab = tk.Label(root, text="探测时间")
cbl21['values'] = n
lab.grid(row=23, column=0)
cbl21.grid(row=23, column=1)

root.mainloop()


