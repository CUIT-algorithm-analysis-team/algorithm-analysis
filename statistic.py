from sort_algorithm import *
from dataset import *
import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s seconds" %
              (str(t1 - t0))
              )
        return result
    return function_timer

@fn_timer
def sort_timer(sort_func,n):
    '''
    :param sort_func: 对应的排序方法
    :param n:  数据规模
    :return: 运行完成的时间
    '''
    d = dataset()
    for l in d.load_data(n):
        l = sort_func(l)
        #print(l)

if __name__ == '__main__':
    sort_timer(select_sort,1000);
