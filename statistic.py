from sort_algorithm import *
from dataset import *
import time
from functools import wraps
import psutil
import gc

sorted_algorithms = {selection_sort:"selection_sort",bubble_sort:"bubble_sort",insertion_sort:"insertion_sort",\
                     merge_sort:"merge_sort",quick_sort:"quick_sort",heap_sort:"heap_sort",shell_sort:"shell_sort",\
                     counting_sort:"counting_sort",radix_sort:"radix_sort"} #


class algorithm_analysis:

    def __init__(self,_sort_algorithms):
        """
        :param _sort_algorithms: 排序算法的列表
        """
        self.sort_algorithms = _sort_algorithms         #各个算法的名字
        self.costed_time = {}                            #用于存储算法对应的时间
        self.costed_space = {}                          #用于存储算法对应的空间
        self.question_size = {}
        for name in list(self.sort_algorithms.values()):
            self.costed_time[name] = []
            self.costed_space[name] = []
            self.question_size[name] = []

    def test_time(self, n, start, step, datastyle):
        """
        测试各个算法所用的时间
        :param n: 数据的规模
        :return: 数据保存再costed_time 里面
        """
        #TODO :后面可以整个进度条
        #选择数据产生方式
        data_loader = dataset.load_data
        if datastyle == "out_order":
            data_loader = dataset.load_data
        elif datastyle == "order":
            data_loader = dataset.load_order_data
        else:
            data_loader = dataset.load_reorder_data

        for i, sort_fun in enumerate(list(self.sort_algorithms.keys())):
            for l in data_loader(n, start, step):
                t0 = time.time()
                result = sort_fun(l)
                t1 = time.time()
                self.costed_time[self.sort_algorithms[sort_fun]].append(t1 - t0)
                self.question_size[self.sort_algorithms[sort_fun]].append(len(l))
                yield i

    def test_space(self,n):
        """
        和时间一样测试算法所用的空间
        :param n: 数据规模
        :return:  数据保存到 costed_space 里面
        """
        p = psutil.Process()  # 获取当前进程
        for sort_fun in list(self.sort_algorithms.keys()):
            for l in dataset.load_data(n):
                result = sort_fun(l)
                t_mem = p.memory_info().wset
                self.costed_space[self.sort_algorithms[sort_fun]].append(t_mem)
                gc.collect()

if __name__ == '__main__':
    a = algorithm_analysis(sorted_algorithms)
    a.test_time(500,"order")
    for func_name , costed_time in a.costed_time.items():
        print(func_name,costed_time[-10:])
