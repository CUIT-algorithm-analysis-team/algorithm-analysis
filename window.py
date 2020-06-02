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
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from  regression_alys import RegressionHelper

imageshow = None
imageregress = None

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.title("algorithm-analysis")
        self.root.geometry('%dx%d' % (800, 600)) #设置窗口大小
        self.imnames = []  #运行的图片结果的名字
        self.data_trans = DataTrans()
        self.createPage()


    def createPage(self):
        # 创建不同Frame
        self.selectPage = selectFrame(self.root, data_trans=self.data_trans)  #算法的选择窗口
        self.regressPage = regressFrame(self.root, data_trans=self.data_trans)  #显示和回归分析窗口
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
        self.regressPage.pack_forget_all()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def regressData(self):
        self.selectPage.pack_forget_all()
        imnames = self.selectPage.run_botton.imnames;
        self.regressPage.getimnames(imnames)   #更新文件名
        self.regressPage.pack_all()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.selectPage.pack_forget_all()
        self.regressPage.pack_forget_all()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.selectPage.pack_forget_all()
        self.regressPage.pack_forget_all()
        self.countPage.pack_forget()
        self.aboutPage.pack()


class selectFrame(Frame):  # 继承Frame类
    def __init__(self, master=None, data_trans=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.imnames = [] #用于存储运行的的结果图的名字
        self.data_trans = data_trans
        self.createPage()
    def createPage(self):
        self.select = select_window(self.root)
        self.seplitline1 = seplit_line(self.root)
        self.numbox = number_box(self.root)  # 数子框
        self.seplitline2 = seplit_line(self.root)
        self.styledata = data_style_box(self.root)  # 数据类型
        self.seplitline3 = seplit_line(self.root)
        self.run_botton = run_botton(self.root, self.select.checkVardict, self.numbox.n, self.numbox.start,
                                     self.numbox.step, self.styledata.var, self.data_trans)

    def pack_all(self):
        self.select.frame_selected.pack()
        self.seplitline1.seplit1.pack(fill=tk.X)
        self.numbox.frame_input_n.pack()
        self.seplitline2.seplit1.pack(fill=tk.X)
        self.styledata.frame_data_style.pack()
        self.seplitline3.seplit1.pack()
        self.run_botton.runbutton.pack()
        self.pack()


    def pack_forget_all(self):
        self.select.frame_selected.pack_forget()
        self.imnames = self.run_botton.imnames; #将值更新回去
        self.seplitline1.seplit1.pack_forget()
        self.numbox.frame_input_n.pack_forget()
        self.seplitline2.seplit1.pack_forget()
        self.styledata.frame_data_style.pack_forget()
        self.seplitline3.seplit1.pack_forget()
        self.run_botton.runbutton.pack_forget()
        self.pack_forget()

class regressFrame(Frame):  # 继承Frame类
    def __init__(self, master=None, data_trans=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.xVariable = StringVar()
        self.imnames = []
        self.data_trans = data_trans
        self.createPage()
        self.createCanvas()

    def createCanvas(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()

    def showChart(self, data):
        fig = self.fig
        canvas=self.canvas
        fig.clear()

        ax = fig.add_subplot(111)

        for item in data.keys():
            ax.plot(data[item]['size'], data[item]['groundtruth'], label=f'{item}')
            ax.plot(data[item]['size'], data[item]['pred'], label=f'{item}_pred')

        ax.legend()
        canvas.draw()


    def showfun(self):
        data = self.data_trans.get_data()

        fig = self.fig
        canvas = self.canvas
        fig.clear()

        ax = fig.add_subplot(111)

        for item in data.sort_algorithms.values():
            ax.plot(data.question_size[item], data.costed_time[item], label=f'{item}')

        ax.legend()
        canvas.draw()

        # imname = self.com.get()
        # global imageshow
        # imageshow = tk.PhotoImage(file=imname)
        # image_label = tk.Label(self, image=imageshow)
        # image_label.pack(side=BOTTOM)

        # img_open = Image.open(imname)
        # img_png = ImageTk.PhotoImage(img_open)
        # label_img = tk.Label(self, image=img_png)
        # label_img.pack()

    def createPage(self):
        self.com = ttk.Combobox(self, textvariable=self.xVariable, width=400)  # #创建下拉菜单
        self.com["value"] = self.imnames  # #给下拉菜单设定值
        self.bu_frame = ttk.Frame(self)
        self.show_bn = ttk.Button(self.bu_frame,text='show',command=self.showfun)
        self.regess_bn = ttk.Button(self.bu_frame,text='regress', command=self.regression_alys)
        self.com.pack()
        self.show_bn.pack( pady=10, side=LEFT)
        # self.regess_bn.pack( pady=10, side=LEFT)
        # self.bu_frame.pack()
        #com.current(0)  #

    def regression_alys(self):
        data = self.data_trans.get_data()
        helper = RegressionHelper(data)
        result = helper.regression()
        self.showChart(data=result)


    def getimnames(self,imnames_):
        self.imnames = imnames_
        self.com["value"] = self.imnames  # #给下拉菜单设定值
        self.com.update()
    def pack_all(self):
        self.com.pack()
        self.show_bn.pack(pady=10, side=LEFT)
        self.regess_bn.pack(pady=10, side=LEFT)
        self.bu_frame.pack()
        self.pack()
    def pack_forget_all(self):
        self.com.pack_forget()
        self.regess_bn.pack_forget()
        self.show_bn.pack_forget()
        self.bu_frame.pack_forget()
        self.pack_forget()

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
        Label(self, text='关于界面\n本系统主要分为了四个页面，分别是：数据录入、显示和回归、统计和关于。\n'
                         '在数据录入页面，用户可以选择一个或者多个想要运行的排序算法，并输入数\n'
                         '据规模和数据显示规则，点击"RUN"按钮，将会显示出所选择的算法根据要求\n'
                         '的输出规则所需的时间曲线。'
                         '在显示和回归页面，用户可以在页面顶部的选择\n'
                         '想要展示的排序算法的时间复杂度拟合的曲线图像。在统计页面，将展示"显示\n'
                         '和回归"中的回归分析所生成的返回结果报告。在关于页面，即本页面，主要用\n'
                         '于展示说明本系统的各项功能和使用方法。', font=('Arial', 12), height =10).pack()
        
class number_box():
    def __init__(self,master):
        self.root = master
        self.frame_input_n = tk.Frame(self.root)
        self.n = tk.StringVar(value=10000)
        self.start = tk.StringVar(value=100)
        self.step = tk.StringVar(value=100)
        self.l = tk.Label(self.frame_input_n, text='请输入数据规模n:', font=('Arial', 12), height=2)
        self.e1 = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=self.n, width=12)  # 输入框
        self.input_start_str = tk.Label(self.frame_input_n, text='初始规模:', font=('Arial', 12), height=2)
        self.input_start_box = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=self.start, width=8)
        self.input_step_str = tk.Label(self.frame_input_n, text='步长:', font=('Arial', 12), height=2)
        self.input_step_box = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=self.step, width=8)

        self.l.pack(side="left")
        self.e1.pack(side="left")
        self.input_start_str.pack(side="left")
        self.input_start_box.pack(side="left")
        self.input_step_str.pack(side="left")
        self.input_step_box.pack(side="left")

class select_window():
    def __init__(self, master=None):
        self.root = master
        self.frame_selected = tk.Frame(self.root)
        listname = list(sorted_algorithms.values())  ##获取函数名字
        group = tk.LabelFrame(self.frame_selected, text='请选中要运行的算法')
        self.checkVardict = {}
        for name in listname:
            self.checkVardict[name] = tk.IntVar(value=0)
        ##selected 绑定在一个frame 里面
        for i in range(3):
            for j in range(3):
                var = self.checkVardict[listname[i * 3 + j]]
                tk.Checkbutton(group, text=listname[i * 3 + j],variable=var,onvalue=1,offvalue=0).grid(row=i, column=j, padx=10, pady=10,
                                                                                   ipadx=10, ipady=10)
        group.pack()
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
        self.var.set("out_order")

class seplit_line():
    #分割线
    def __init__(self,master):
        self.root = master
        self.seplit1 = ttk.Separator(self.root, orient='horizontal')  ##这是分割线
        #self.seplit1.pack(fill=tk.X)

class run_botton():
    def __init__(self,master, checkVardict, n, start, step, datastyle, data_trans):
        self.root = master
        self.num = n #数据的规模
        self.start = start
        self.step = step
        self.datastyle = datastyle
        self.checkVardict = checkVardict #多选框的值
        self.selected_dict = {}
        self.imnames = []  #用于保存生成的图片的名字
        self.runbutton = tk.Button(self.root, text='RUN', font=('Arial', 12), width=10, height=1, command=self.run)
        self.data_trans = data_trans

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
        start = int(self.start.get())
        step = int(self.step.get())

        popup = tk.Toplevel()
        tk.Label(popup, text="程序正在运行").grid(row=0, column=0)
        progress = 0
        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=len(list(a.sort_algorithms.keys())) - 1)
        progress_bar.grid(row=1, column=0)  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
        popup.pack_slaves()
        for i in a.test_time(n, start, step, self.datastyle.get()):        #计算运行的时间
            popup.update()
            progress = i;
            progress_var.set(progress)

        print("success")

        self.data_trans.set_data(a)

        # try:
        #     ##把图片画回去
        #     drawCostTime(a.costed_time,int(self.num.get()),self.imnames[-1])
        # except:
        #     messagebox.showinfo(title='保存图片出错', message=self.imnames[-1])

    def show(self):
        ls = ""
        for name, value in self.checkVardict.items():
            if value.get() == 1:
                ls += "/ " + name
        ls += "\n"
        ls += "the value is %s\n"%self.num.get()
        ls += "the datastyle %s\n"%self.datastyle.get()
        messagebox.showinfo(title='不知道起什么', message=ls)


class DataTrans():
    def __init__(self):
        self.data = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

if __name__ == '__main__':
    mi = MainPage(tk.Tk())#
    # imageshow = tk.PhotoImage(file="merge_sort_quick_sort_10_out_order.png")
    # image_label = tk.Label(mi, image=imageshow)
    # image_label.pack()
    mi.root.mainloop()
