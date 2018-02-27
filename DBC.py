# import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

root=Tk()
stdpointfieldname=['物探点号','特征点','附属物']
stdlinefieldname=['起点点号','终点点号','起点高程','终点高程','起点埋深','终点埋深']
# 将self.orderDict中的信息写入本地xml文件，参数filename是xml文件名
def getallfield(root,self):
    n = []
    for (k, v) in self.items():
        n.append(k + " " + v)
    # print(n)

    m={}
    def go(*args):
        m["物探点号"]=cbl1.get()
        m["图上点号"]=cbl2.get()
        m["特征点"]=cbl3.get()
        m["附属物"]=cbl4.get()
        m["X坐标"]=cbl5.get()
        m["Y坐标"]=cbl6.get()
        m["管线性质"]=cbl7.get()
        m["地面高程"]=cbl8.get()
        m["井底深"]=cbl9.get()
        m["井盖规格"]=cbl10.get()
        m["井盖类型"]=cbl11.get()
        m["井盖材质"]=cbl12.get()
        m["井盖附属物代码"]=cbl13.get()
        m["井室规格"]=cbl14.get()
        m["井室角度"]=cbl15.get()
        m["井盖照片代码"]=cbl16.get()
        m["图幅号"]=cbl17.get()
        m["偏心井位"]=cbl18.get()
        m["所在道路"]=cbl19.get()
        m["探测单位"]=cbl20.get()
        m["探测时间"]=cbl21.get()
        m["备注"]=cbl22.get()
        # 删除字典中值为空的元素
        m_key=list(m.keys())
        for m_s in m_key:
            if m[m_s]== "":
                m.pop(m_s)
        return
        print(m)

    btn = ttk.Button(root, text="确定", command=go)
    btn.grid(row=0,column=0)

    lab = Label(root, text="物探点号")
    lab.grid(row=1,column=0)
    cbl1 = ttk.Combobox(root, textvariable=StringVar())
    cbl1.grid(row=1,column=1)
    cbl1['values'] = n

    cbl2 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="图上点号")
    cbl2['values'] = n
    lab.grid(row=2, column=0)
    cbl2.grid(row=2, column=1)

    cbl3 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="特征点")
    cbl3['values'] = n
    lab.grid(row=3, column=0)
    cbl3.grid(row=3, column=1)

    cbl4 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="附属物")
    cbl4['values'] = n
    lab.grid(row=4, column=0)
    cbl4.grid(row=4, column=1)

    cbl5 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="X坐标")
    cbl5['values'] = n
    lab.grid(row=5, column=0)
    cbl5.grid(row=5, column=1)

    cbl6 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="Y坐标")
    cbl6['values'] = n
    lab.grid(row=6, column=0)
    cbl6.grid(row=6, column=1)

    cbl7 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="管线性质")
    cbl7['values'] = n
    lab.grid(row=7, column=0)
    cbl7.grid(row=7, column=1)

    cbl8 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="地面高程")
    cbl8['values'] = n
    lab.grid(row=8, column=0)
    cbl8.grid(row=8, column=1)

    cbl9 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井底深")
    cbl9['values'] = n
    lab.grid(row=9, column=0)
    cbl9.grid(row=9, column=1)

    cbl10 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井盖规格")
    cbl10['values'] = n
    lab.grid(row=10, column=0)
    cbl10.grid(row=10, column=1)

    cbl11 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井盖类型")
    cbl11['values'] = n
    lab.grid(row=11, column=0)
    cbl11.grid(row=11, column=1)

    cbl12 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井盖材质")
    cbl12['values'] = n
    lab.grid(row=12, column=0)
    cbl12.grid(row=12, column=1)

    cbl13 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井室附属物代码")
    cbl13['values'] = n
    lab.grid(row=13, column=0)
    cbl13.grid(row=13, column=1)

    cbl14 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井室规格")
    cbl14['values'] = n
    lab.grid(row=14, column=0)
    cbl14.grid(row=14, column=1)

    cbl15 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井室角度")
    cbl15['values'] = n
    lab.grid(row=15, column=0)
    cbl15.grid(row=15, column=1)

    cbl16 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="井盖照片代码")
    cbl16['values'] = n
    lab.grid(row=16, column=0)
    cbl16.grid(row=16, column=1)

    cbl17 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="图幅号")
    cbl17['values'] = n
    lab.grid(row=17, column=0)
    cbl17.grid(row=17, column=1)

    cbl18 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="偏心井位")
    cbl18['values'] = n
    lab.grid(row=18, column=0)
    cbl18.grid(row=18, column=1)

    cbl19 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="所在道路")
    cbl19['values'] = n
    lab.grid(row=19, column=0)
    cbl19.grid(row=19, column=1)

    cbl20 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="探测单位")
    cbl20['values'] = n
    lab.grid(row=20, column=0)
    cbl20.grid(row=20, column=1)

    cbl21 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="探测时间")
    cbl21['values'] = n
    lab.grid(row=21, column=0)
    cbl21.grid(row=21, column=1)

    cbl22 = ttk.Combobox(root, textvariable=StringVar())
    lab = Label(root, text="备注")
    cbl22['values'] = n
    lab.grid(row=22, column=0)
    cbl22.grid(row=22, column=1)
    # root.mainloop()
