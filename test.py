from tkinter import *
import tkinter as tk
import time
import tkinter.messagebox as messagebox
class progress_bar():
    def __init__(self,master):
        # 进度条
        # 更新进度条函数
        # 创建画布
        self.root = master
        self.frame = Frame(self.root)  # 使用时将框架根据情况选择新的位置
        self.canvas = Canvas(self.frame, width=120, height=30, bg="white")
        self.canvas.grid(row=0, column=0)
        self.x = tk.StringVar()
        # 进度条以及完成程度
        self.out_rec = self.canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
        self.fill_rec = self.canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")
        self.l = tk.Label(self.frame, textvariable=self.x)
    def change_schedule(self, flag, now_schedule,all_schedule):
        if flag == 1:
            self.canvas.coords(self.fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))
            self.root.update()
            self.x.set(str(round(now_schedule/all_schedule*100,2)) + '%')
            if round(now_schedule/all_schedule*100,2) == 100.00:
                self.x.set("完成")
        else:
            self.canvas.coords(self.fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 100, 25))
            self.root.update()


'''
使用时直接调用函数change_schedule(now_schedule,all_schedule)
下面就模拟一下....
'''
def showbar():
    messagebox.showinfo()
    Tk.showinfo(title='新窗口', message='另一个窗口')
if __name__ == '__main__':
    # # root = Tk()
    # # root.title("algorithm-analysis")
    # # root.geometry('%dx%d' % (600, 400))
    # # button = tk.Button(root, text='bar', font=('Arial', 12), width=10, height=1, command=showbar)
    # # button.pack()
    # # bar = progress_bar(root)
    # # for i in range(100):
    # #     time.sleep(0.1)
    # #     bar.change_schedule(0,i, 99)
    # root.mainloop()
    root = Tk()


    def command():
        top = Toplevel()
        top.title('运行中...')
        bar = progress_bar(top)
        bar.frame.pack()
        for i in range(100):
            time.sleep(0.1)
            bar.change_schedule(0,i, 99)

    button = Button(root, text="New Window", command=command)
    button.pack()

    root.mainloop()