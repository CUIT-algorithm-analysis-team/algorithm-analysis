import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import Canvas
from statistic import sorted_algorithms , algorithm_analysis
import time
import PIL
from PIL import ImageTk
from drawing import *
class basedesk():
    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("algorithm-analysis")
        self.root.geometry('500x700')
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        #选择窗口
        selectw = select_window(self.root)
        seplit_line(self.root) #分割线
        numbox = number_box(self.root)  #数子框
        seplit_line(self.root)  # 分割线
        styledata = data_style_box(self.root) #数据类型
        seplit_line(self.root)  # 分割线
        b = run_botton(self.root,selectw.checkVardict,numbox.n,styledata.var)
        b.pack()
        bar = progress_bar(self.root)
        seplit_line(self.root)  # 分割线
        tag_box(self.root,b.imnames)     #选择框
        ##选择框的内容
    def run(self):
        self.root.mainloop()

class select_window():
    def __init__(self,master):
        self.root = master
        self.frame_selected = tk.Frame(self.root)
        self.frame_selected.pack()
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
class seplit_line():
    #分割线
    def __init__(self,master):
        self.root = master
        self.seplit1 = ttk.Separator(self.root, orient='horizontal')  ##这是分割线
        self.seplit1.pack(fill=tk.X)
class number_box():
    def __init__(self,master):
        self.root = master
        self.frame_input_n = tk.Frame(self.root)
        self.frame_input_n.pack()
        self.n = tk.StringVar(value=10000)
        self.l = tk.Label(self.frame_input_n, text='请输入数据规模n:', font=('Arial', 12), height=2)
        self.e1 = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=self.n)  # 输入框
        self.e1.pack(side="right")
        self.l.pack(side="left")

class data_style_box():
    def __init__(self,master):
        self.root = master
        # 创建选择窗口
        frame_data_style = tk.Frame(self.root)
        frame_data_style.pack()
        self.var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
        # 创建单选框
        self.r1 = tk.Radiobutton(frame_data_style, text='乱序', variable=self.var, value='out_order', command=None)
        self.r1.grid(row=0, column=0)
        self.r2 = tk.Radiobutton(frame_data_style, text='顺序', variable=self.var, value='order', command=None)
        self.r2.grid(row=0, column=1)
        self.r3 = tk.Radiobutton(frame_data_style, text='逆序', variable=self.var, value='reorder', command=None)
        self.r3.grid(row=0, column=2)
class run_botton():
    def __init__(self,master, checkVardict, n, datastyle):
        self.root = master
        self.num = n #数据的规模
        self.datastyle = datastyle
        self.checkVardict = checkVardict #多选框的值
        self.selected_dict = {}
        self.imnames = []  #用于保存生成的图片的名字

        self.b = tk.Button(self.root, text='RUN', font=('Arial', 12), width=10, height=1, command=self.run)
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
    def pack(self):
        self.b.pack()
class progress_bar():
    def __init__(self,master):
        # 进度条
        # 更新进度条函数
        # 创建画布
        self.root = master
        frame_propression = tk.Frame(self.root).pack()  # 使用时将框架根据情况选择新的位置
        self.canvas = Canvas(frame_propression, width=120, height=30, bg="white")
        self.canvas.pack()
        self.x = tk.StringVar()
        # 进度条以及完成程度
        self.out_rec = self.canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        self.fill_rec = self.canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")
        self.l = tk.Label(frame_propression, textvariable=self.x)
    def change_schedule(self,now_schedule,all_schedule):
        self.canvas.coords(self.fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))
        self.root.update()
        self.x.set(str(round(now_schedule/all_schedule*100,2)) + '%')
        if round(now_schedule/all_schedule*100,2) == 100.00:
            self.x.set("完成")

class time_tag():
    def __init__(self,master):
        # frame_time --> 时间显示
        self.root = master
        self.frame_time = tk.Frame(self.root, height=300) #bg="red"
        self.frame_time.pack(side=tk.TOP, fill=tk.X)
        self.label = tk.Label(self.frame_time)

class space_tag():
    def __init__(self,master):
        # frame_space --> 空间显示
        self.root = master
        self.frame_space = tk.Frame(self.root, height=350, bg="blue")
        self.frame_space.pack(side=tk.TOP, fill=tk.X)
class regression_tag():
    def __init__(self,master):
        # frame5 --> 回归分析
        self.root = master
        self.frame_regress = tk.Frame(self.root, height=350, bg="yellow")
        self.frame_regress.pack(side=tk.TOP, fill=tk.X)

class tag_box():
    def __init__(self,master,imnames):
        self.root = master
        self.imnames = imnames  #获取到图片的文件
        frame_tag = tk.Frame(self.root)
        frame_tag.pack(fill=tk.Y, pady=10)
        self.tag = tk.IntVar()
        tagWidth = 23

        tk.Radiobutton(frame_tag, text="运行时间", command=lambda: self.changeTag(0), width=tagWidth, variable=self.tag,
                            value=0,
                            bd=1,
                            indicatoron=0).grid(column=0, row=1)
        tk.Radiobutton(frame_tag, text="使用空间", command=lambda: self.changeTag(1), variable=self.tag, width=tagWidth,
                            value=1,
                            bd=1,
                            indicatoron=0).grid(column=1, row=1)
        tk.Radiobutton(frame_tag, text="时间复杂度", command=lambda: self.changeTag(2), variable=self.tag, width=tagWidth,
                            value=2,
                            bd=1,
                            indicatoron=0).grid(column=2, row=1)

        self.time_tag = time_tag(master)
        self.space_tag = space_tag(master)
        self.regress_tag = regression_tag(master)
        self.img = None
    def changeTag(self,tag):
        if tag == 0:
            if self.imnames[-1] is not None:
                imname = self.imnames[-1]  #读出最近的一个图片
                im = PIL.Image.open(imname)
                im = im.resize((500, 300), PIL.Image.ANTIALIAS)  # 图片改变大小以适应tag框
                self.img = ImageTk.PhotoImage(im)
                self.time_tag.label.configure(image=self.img)
                # try:
                #     time_tag(self.root,imname)
                # except:
                #     messagebox.showinfo(title='画图错误', message="在显示图片的时候出现了错误")
        elif tag == 1:
            self.frame_space.pack(fill=tk.X)
        elif tag == 2:
            self.frame_regress.pack(fill=tk.X)
        self.root.update()
if __name__ == '__main__':
    mi = basedesk()
    mi.run()