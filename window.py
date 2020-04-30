import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from statistic import sorted_algorithms
import time

window = tk.Tk()

window.title("algorithm-analysis")

window.geometry('500x700')
frame_selected = tk.Frame(window)
frame_selected.pack()

listname = list(sorted_algorithms.values())
##selected 绑定在一个frame 里面
for i in range(3):
    for j in range(3):
        tk.Checkbutton(frame_selected, text=listname[i * 3 + 1]).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)

seplit1=ttk.Separator(window,orient='horizontal')  ##这是分割线
seplit1.pack(fill=tk.X)

frame_input_n = tk.Frame(window)
frame_input_n.pack()

n = tk.StringVar(value=10000)
l = tk.Label(frame_input_n, text='请输入数据规模n:',font=('Arial', 12), height=2)
e1 = tk.Entry(frame_input_n, show=None, font=('Arial', 14),textvariable=n)   # 输入框
e1.pack(side="right")
l.pack(side="left")
seplit2=ttk.Separator(window,orient='horizontal')  ##这是分割线
seplit2.pack(fill=tk.X)

frame_data_style = tk.Frame(window)
frame_data_style.pack()
var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
#创建单选框
r1 = tk.Radiobutton(frame_data_style, text='乱序', variable=var, value='A', command=None)
r1.grid(row = 0,column=0)
r2 = tk.Radiobutton(frame_data_style, text='顺序', variable=var, value='B', command=None)
r2.grid(row = 0,column=1)
r3 = tk.Radiobutton(frame_data_style, text='逆序', variable=var, value='C', command=None)
r3.grid(row = 0,column=2)
seplit3=ttk.Separator(window,orient='horizontal')  ##这是分割线
seplit3.pack(fill=tk.X)
#按钮
def run():  #只是测试一下
    for i in range(100):
        time.sleep(0.1)
        change_schedule(i, 99)

b = tk.Button(window, text='RUN', font=('Arial', 12), width=10, height=1, command=run)
b.pack()
seplit4=ttk.Separator(window,orient='horizontal')  ##这是分割线
seplit4.pack(fill=tk.X)
#进度条
#更新进度条函数


def change_schedule(now_schedule,all_schedule):
    canvas.coords(fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))
    window.update()
    x.set(str(round(now_schedule/all_schedule*100,2)) + '%')
    if round(now_schedule/all_schedule*100,2) == 100.00:
        x.set("完成")
# 创建画布
frame_propression = tk.Frame(window).pack()  # 使用时将框架根据情况选择新的位置
canvas = Canvas(frame_propression, width=120, height=30, bg="white")
canvas.pack()
x = tk.StringVar()
# 进度条以及完成程度
out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")

l = tk.Label(frame_propression, textvariable=x)
seplit5=ttk.Separator(window,orient='horizontal')  ##这是分割线
seplit5.pack(fill=tk.X)

window.mainloop()