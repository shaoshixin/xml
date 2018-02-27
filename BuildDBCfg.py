from xml.dom.minidom import Document
import tkinter
from tkinter import ttk

tk=tkinter.Tk()
stdpointfieldname=['物探点号','特征点','附属物']
stdlinefieldname=['起点点号','终点点号','起点高程','终点高程','起点埋深','终点埋深']
# 将self.orderDict中的信息写入本地xml文件，参数filename是xml文件名
def writeInfoToXml(self,where,bool):
    # 创建dom文档
    doc = Document()
    # 创建根节点
    config = doc.createElement('Config')
    # 根节点插入dom树
    doc.appendChild(config)
    scheme=doc.createElement('Scheme')
    scheme.setAttribute('Name',where + '管线成图方案')
    scheme.setAttribute('Description',where + '管线成图方案')
    scheme.setAttribute('DealHField',bool)
    config.appendChild(scheme)

    # 依次将orderDict中的每一组元素提取出来，创建对应节点并插入dom树
    # 创建节点<PointFields>
    pointfields = doc.createElement('PointFields')
    scheme.appendChild(pointfields)


    for k in ["A","B","C"]:
        def go(*args):
            # com["l"]=comboxlist.get()
            print("comboxlistvalue:" + comboxlist.get())
        comvalue = tkinter.StringVar()
        comboxlist = ttk.Combobox(tk, textvariable=comvalue)
        lab=tkinter.Label(tk,text=k)
        comboxlist['values']=["a","b","c"]
        # comboxlist.current(0)
        # comboxlist.bind("<<ComboboxSelected>>",lambda k:go(k))
        lab.pack()
        comboxlist.pack()
        btn = ttk.Button(tk, text="确定", command=go)
        btn.pack()

        # field = doc.createElement('Field')
        # field.setAttribute('Source',sur)
        # field.setAttribute('Standard', sur)
        # field.setAttribute('type',tp)
        # pointfields.appendChild(field)
    # 将电话插入<LineFields>中，处理同上

    linefields = doc.createElement('LineFields')
    scheme.appendChild(linefields)

    for k in self:
        # (name, tel, addr, cnt) = (self[0], self[1], self[2], self[3])

        field = doc.createElement('Field')
        field.setAttribute('Source',k)
        field.setAttribute('Standard',k)
        linefields.appendChild(field)

    # 将地址插入<PointLayers>中，处理同上
    pointlayers = doc.createElement('PointLayers')
    scheme.appendChild(pointlayers)
    for k in self:
        # (name, tel, addr, cnt) = (self[0], self[1], self[2], self[3])
        field = doc.createElement('Field')
        field.setAttribute('Source',k)
        field.setAttribute('Standard',k)
        pointlayers.appendChild(field)

    # 将点餐次数插入<LineLayers>中，处理同上
    linelayers = doc.createElement('LineLayers')
    scheme.appendChild(linelayers)
    for k in self:
        # (name, tel, addr, cnt) = (self[0], self[1], self[2], self[3])
        field = doc.createElement('Field')
        field.setAttribute('Source',k)
        field.setAttribute('Standard',k)
        linelayers.appendChild(field)

    # 将dom对象写入本地xml文件
    f = open('BuildDBCfg.xml', 'w')
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
    f.close()

    return