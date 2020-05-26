import matplotlib.pyplot as plt
import numpy as np

def drawCostTime(costed_time,n,imgname):
    """
    绘制曲线图
    :param costed_time : 算法和时间对应的字典类型
    :param n: 数据规模作为横轴
    :return: TODO：将图片给嵌入到后续的界面上去
    """
    fig = plt.figure()
    ax = plt.subplot(111)
    x = np.arange(1,n + 1)
    for func_name ,time in costed_time.items():
        plt.plot(x,time,label=func_name)
    plt.legend()
    plt.savefig(imgname)  #尝试保存图片