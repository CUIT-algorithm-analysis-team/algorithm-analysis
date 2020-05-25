import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import Canvas
from statistic import sorted_algorithms , algorithm_analysis
import time
import PIL
from PIL import ImageTk
from drawing import *
from tkinter import *
from tkinter.messagebox import *


class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.title("algorithm-analysis")
        self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小
        self.imnames = []  #运行的图片结果的名字
        self.createPage()

    def createPage(self):
        # 创建不同Frame
        self.selectPage = selectFrame(self.root)  #算法的选择窗口
        self.regressPage = regressFrame(self.root)  #显示和回归分析窗口
        self.countPage = CountFrame(self.root)    #统计窗口
        self.aboutPage = AboutFrame(self.root)    #相关窗口
        self.selectPage.pack_all()  # 默认显示数据录入界面
        menubar = tk.Menu(self.root)
        menubar.add_command(label='数据录入', command=self.selectData)
        menubar.add_command(label='显示和回归', command=self.regressData)
        menubar.add_command(label='统计', command=self.countData)
        menubar.add_command(label='关于', command=self.aboutDisp)
        self.root['menu'] = menubar  # 设置菜单栏
    def selectData(self):
        self.selectPage.pack_all()
        self.regressPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def regressData(self):
        self.selectPage.pack_forget_all()
        imnames = self.selectPage.run_botton.imnames;
        self.regressPage.getimnames(imnames)   #获取select 的操作
        self.regressPage.pack()
        self.regressPage.createPage()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.selectPage.pack_forget()
        self.regressPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.selectPage.pack_forget()
        self.regressPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()


class selectFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.imnames = [] #用于存储运行的的结果图
        self.createPage()
    def createPage(self):
        self.select = select_window(self.root)
        self.seplitline1 = seplit_line(self.root)
        self.numbox = number_box(self.root)  # 数子框
        self.seplitline2 = seplit_line(self.root)
        self.styledata = data_style_box(self.root)  # 数据类型
        self.seplitline3 = seplit_line(self.root)
        self.run_botton = run_botton(self.root, self.select.checkVardict, self.numbox.n, self.styledata.var)
        self.bar = progress_bar(self.root)

    def pack_all(self):
        self.select.frame_selected.pack()
        self.seplitline1.seplit1.pack(fill=tk.X)
        self.numbox.frame_input_n.pack()
        self.seplitline2.seplit1.pack(fill=tk.X)
        self.styledata.frame_data_style.pack()
        self.seplitline3.seplit1.pack()
        self.run_botton.runbutton.pack()
        self.bar.frame_propression.pack()
        self.bar.canvas.pack()
        self.pack()


    def pack_forget_all(self):
        self.select.frame_selected.pack_forget()
        self.imnames = self.run_botton.imnames; #将值更新回去
        self.seplitline1.seplit1.pack_forget()
        self.numbox.frame_input_n.pack_forget()
        self.pack_forget()
        self.seplitline2.seplit1.pack_forget()
        self.styledata.frame_data_style.pack_forget()
        self.seplitline3.seplit1.pack_forget()
        self.run_botton.runbutton.pack_forget()
        self.bar.frame_propression.pack_forget()
        self.bar.canvas.pack_forget()

class regressFrame(Frame):  # 继承Frame类
    def __init__(self, master=None,):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.xVariable = StringVar()
        self.imnames = []
        #self.createPage()


    def createPage(self):
        com = ttk.Combobox(self, textvariable=self.xVariable,width = 400)  # #创建下拉菜单
        #从
        com["value"] = self.imnames #("河北", "河南", "山东")  # #给下拉菜单设定值
        #com.current(0)  # #设定下拉菜单的默认值为第3个，即山东
        com.pack()
        Label(self, text='显示和回归界面').pack()
        #com.bind("<<ComboboxSelected>>", self.drawfun)

    def getimnames(self,imnames_):
        self.imnames = imnames_


class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='统计界面').pack()


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()
    def createPage(self):
        Label(self, text='关于界面').pack()

class number_box():
    def __init__(self,master):
        self.root = master
        self.frame_input_n = tk.Frame(self.root)
        self.n = tk.StringVar(value=10000)
        self.l = tk.Label(self.frame_input_n, text='请输入数据规模n:', font=('Arial', 12), height=2)
        self.e1 = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=self.n)  # 输入框
        self.e1.pack(side="right")
        self.l.pack(side="left")


class select_window():
    def __init__(self, master=None):
        self.root = master
        self.frame_selected = tk.Frame(self.root)
        listname = list(sorted_algorithms.values())  ##获取函数名字
        self.checkVardict = {}
        for name in listname:
            self.checkVardict[name] = tk.IntVar(value=0)
        ##selected 绑定在一个frame 里面
        for i in range(3):
            for j in range(3):
                var = self.checkVardict[listname[i * 3 + j]]
                tk.Checkbutton(self.frame_selected, text=listname[i * 3 + j],variable=var,onvalue=1,offvalue=0).grid(row=i, column=j, padx=10, pady=10,
                                                                                   ipadx=10, ipady=10)
class data_style_box():
    def __init__(self,master):
        self.root = master
        # 创建选择窗口
        self.frame_data_style = tk.Frame(self.root)
        self.var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
        # 创建单选框
        self.r1 = tk.Radiobutton(self.frame_data_style, text='乱序', variable=self.var, value='out_order', command=None)
        self.r1.grid(row=0, column=0)
        self.r2 = tk.Radiobutton(self.frame_data_style, text='顺序', variable=self.var, value='order', command=None)
        self.r2.grid(row=0, column=1)
        self.r3 = tk.Radiobutton(self.frame_data_style, text='逆序', variable=self.var, value='reorder', command=None)
        self.r3.grid(row=0, column=2)

class seplit_line():
    #分割线
    def __init__(self,master):
        self.root = master
        self.seplit1 = ttk.Separator(self.root, orient='horizontal')  ##这是分割线
        #self.seplit1.pack(fill=tk.X)

class run_botton():
    def __init__(self,master, checkVardict, n, datastyle):
        self.root = master
        self.num = n #数据的规模
        self.datastyle = datastyle
        self.checkVardict = checkVardict #多选框的值
        self.selected_dict = {}
        self.imnames = []  #用于保存生成的图片的名字
        self.runbutton = tk.Button(self.root, text='RUN', font=('Arial', 12), width=10, height=1, command=self.run)
    def run(self):  #只是测试一下
        #生成图片的名字
        ls = ""
        for name, value in self.checkVardict.items():
            if value.get() == 1:
                ls += name + "_"
        ls += self.num.get() + "_"
        ls += self.datastyle.get() + ".png"
        if ls not in self.imnames:
            self.imnames.append(ls)
        # 从checkVardict中得到选中的func 和 name的字典
        for func , name in sorted_algorithms.items():
            if self.checkVardict[name].get() == 1:
                self.selected_dict[func] = name
        a = algorithm_analysis(self.selected_dict)
        n = int(self.num.get())
        a.test_time(n,self.datastyle.get())  #计算运行的时间
        try:
            ##把图片画回去
            drawCostTime(a.costed_time,int(self.num.get()),self.imnames[-1])
        except:
            messagebox.showinfo(title='保存图片出错', message=self.imnames[-1])

    def show(self):
        ls = ""
        for name, value in self.checkVardict.items():
            if value.get() == 1:
                ls += "/ " + name
        ls += "\n"
        ls += "the value is %s\n"%self.num.get()
        ls += "the datastyle %s\n"%self.datastyle.get()
        messagebox.showinfo(title='不知道起什么', message=ls)

class progress_bar():
    def __init__(self,master):
        # 进度条
        # 更新进度条函数
        # 创建画布
        self.root = master
        self.frame_propression = tk.Frame(self.root)  # 使用时将框架根据情况选择新的位置
        self.canvas = Canvas(self.frame_propression, width=120, height=30, bg="white")
        self.x = tk.StringVar()
        # 进度条以及完成程度
        self.out_rec = self.canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        self.fill_rec = self.canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")
        self.l = tk.Label(self.frame_propression, textvariable=self.x)
    def change_schedule(self,now_schedule,all_schedule):
        self.canvas.coords(self.fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))
        self.root.update()
        self.x.set(str(round(now_schedule/all_schedule*100,2)) + '%')
        if round(now_schedule/all_schedule*100,2) == 100.00:
            self.x.set("完成")

if __name__ == '__main__':
    mi = MainPage(tk.Tk())
    mi.root.mainloop()
