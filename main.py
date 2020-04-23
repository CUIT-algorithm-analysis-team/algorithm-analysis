from dataset import *
from drawing import *
from sort_algorithm import *
from statistic import *

if __name__ == '__main__':
    a = algorithm_analysis(sorted_algorithms)
    a.test_time(1000)
    drawCostTime(a.costed_time,1000)