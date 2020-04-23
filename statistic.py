from sort_algorithm import *
from dataset import *
import time
from functools import wraps

sorted_algorithms = {select_sort:"select_sort",bubble_sort:"bubble_sort"}

class algorithm_analysis:
    def __init__(self,_sort_algorithms):
        """
        :param _sort_algorithms: 排序算法的列表
        """
        self.sort_algorithms = _sort_algorithms         #各个算法的名字
        self.costed_time = {}                            #用于存储算法对应的时间
        self.costed_space = {}                          #用于存储算法对应的空间
        for name in list(self.sort_algorithms.values()):
            self.costed_time[name] = []
            self.costed_space[name] = []
    def test_time(self,n):
        """
        测试各个算法所用的时间
        :param n: 数据的规模
        :return: 数据保存再costed_time 里面
        """
        #TODO :后面可以整个进度条
        for sort_fun in list(self.sort_algorithms.keys()):
            for l in dataset.load_data(n):
                t0 = time.time()
                result = sort_fun(l)
                t1 = time.time()
                self.costed_time[self.sort_algorithms[sort_fun]].append(t1 - t0)

if __name__ == '__main__':
    a = algorithm_analysis(sorted_algorithms)
    a.test_time(1000)
    for func_name , cost_time in a.costed_time.items():
        print(func_name,cost_time[-5:])
