import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from statistic import sorted_algorithms
import time
import PIL
from PIL import ImageTk

class basedesk():
    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("algorithm-analysis")
        self.root.geometry('500x700')
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        #选择窗口
        select_window(self.root)
        seplit_line(self.root) #分割线
        number_box(self.root)  #数子框
        seplit_line(self.root)  # 分割线
        data_style_box(self.root) #数据类型
        seplit_line(self.root)  # 分割线
        b = run_botton(self.root)
        b.pack()
        bar = progress_bar(self.root)
        seplit_line(self.root)  # 分割线
        tag_box(self.root)     #选择框
        ##选择框的内容


    def run(self):
        self.root.mainloop()

class select_window():
    def __init__(self,master):
        self.root = master
        self.frame_selected = tk.Frame(self.root)
        self.frame_selected.pack()
        listname = list(sorted_algorithms.values())  ##获取函数名字
        ##selected 绑定在一个frame 里面
        for i in range(3):
            for j in range(3):
                tk.Checkbutton(self.frame_selected, text=listname[i * 3 + 1]).grid(row=i, column=j, padx=10, pady=10,
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

        n = tk.StringVar(value=10000)
        self.l = tk.Label(self.frame_input_n, text='请输入数据规模n:', font=('Arial', 12), height=2)
        self.e1 = tk.Entry(self.frame_input_n, show=None, font=('Arial', 14), textvariable=n)  # 输入框
        self.e1.pack(side="right")
        self.l.pack(side="left")

class data_style_box():
    def __init__(self,master):
        self.root = master
        # 创建选择窗口
        frame_data_style = tk.Frame(self.root)
        frame_data_style.pack()
        var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
        # 创建单选框
        self.r1 = tk.Radiobutton(frame_data_style, text='乱序', variable=var, value='A', command=None)
        self.r1.grid(row=0, column=0)
        self.r2 = tk.Radiobutton(frame_data_style, text='顺序', variable=var, value='B', command=None)
        self.r2.grid(row=0, column=1)
        self.r3 = tk.Radiobutton(frame_data_style, text='逆序', variable=var, value='C', command=None)
        self.r3.grid(row=0, column=2)
class run_botton():
    def __init__(self,master,func=None):
        self.root = master
        self.func = func
        self.b = tk.Button(self.root, text='RUN', font=('Arial', 12), width=10, height=1, command=None)
    def run(self):  #只是测试一下
        for i in range(100):
            time.sleep(0.1)
            self.func(i, 99)
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
        self.frame_time = tk.Frame(self.root, height=300, bg="red")
        self.frame_time.pack(side=tk.TOP, fill=tk.X)
        self.im = PIL.Image.open("plottext.png")
        self.im = self.im.resize((500, 300), PIL.Image.ANTIALIAS)  # 图片改变大小以适应tag框
        self.img = ImageTk.PhotoImage(self.im)
        self.imLabel = tk.Label(self.frame_time, image=self.img).pack()  # 显示图片
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
    def __init__(self,master,):
        self.root = master
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

        self.frame_time = time_tag(master)
        self.frame_space = space_tag(master)
        self.frame_regress = regression_tag(master)

    def changeTag(self,tag):
        self.frame_time.pack_forget()
        self.frame_space.pack_forget()
        self.frame_regress.pack_forget()
        if tag == 0:
            self.frame_time.pack(fill=tk.X)
        elif tag == 1:
            self.frame_space.pack(fill=tk.X)
        elif tag == 2:
            self.frame_regress.pack(fill=tk.X)

if __name__ == '__main__':
    mi = basedesk()
    mi.run()