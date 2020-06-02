import numpy as np
from scipy.optimize import least_squares


class RegressionHelper():
    def __init__(self, data):
        self.data = data
        self.result = None
        self.sort_algorithms = data.sort_algorithms
        self.costed_time = data.costed_time
        self.question_size = data.question_size

    def regression(self):
        """
        Regression Analysis.
        :return: A dict.{'type': str 'nlogn' or 'n2',
                         'cost': float,
                         'pred': list,
                         'param': tuple(a, b)  nlogn is (a*nlogn + b). n2 is  (a*n^2 + b)}
        """
        out = {}
        for item in self.sort_algorithms.values():
            out[item] = {}
            nlogn = least_squares(residuals_nlogn, [1, 1],
                                  args=(np.array(self.costed_time[item]),
                                        np.array(self.question_size[item])))
            n2 = least_squares(residuals_n2, [1, 1],
                               args=(np.array(self.costed_time[item]),
                                     np.array(self.question_size[item])))

            if nlogn['cost'] < n2['cost']:
                pred_time_nlogn = nlogn['x'][0] * np.array(self.question_size[item]) \
                                  * np.log(self.question_size[item]) + nlogn['x'][1]
                out[item]['type'] = 'nlogn'
                out[item]['cost'] = round(nlogn['cost'], 6)
                out[item]['pred'] = pred_time_nlogn.tolist()
                out[item]['groundtruth'] = self.costed_time[item]
                out[item]['param'] = (nlogn['x'][0], nlogn['x'][1])
            else:
                pred_time_n2 = n2['x'][0] * np.power(np.array(self.question_size[item]), 2) + n2['x'][1]
                out[item]['type'] = 'n2'
                out[item]['cost'] = round(n2['cost'], 6)
                out[item]['pred'] = pred_time_n2.tolist()
                out[item]['groundtruth'] = self.costed_time[item]
                out[item]['param'] = (n2['x'][0], n2['x'][1])

        self.result = out
        return out


def residuals_nlogn(param, y, x):
    a, b = param
    return y - (a * x * np.log(x) + b)


def residuals_n2(param, y, x):
    a, b = param
    return y - (a * np.power(x, 2) + b)


if __name__ == '__main__':
    from dataset import dataset
    from sort_algorithm import *
    from statistic import algorithm_analysis
    import time
    import matplotlib.pyplot as plt
    from tqdm import tqdm

    data = dataset()
    algorithm_dict = {quick_sort:"quick_sort", bubble_sort:"bubble_sort"}
    run_algo = algorithm_analysis(algorithm_dict)
    for i in run_algo.test_time(1000, 100, 100, 'out_order'):
        pass

    reg_alys = RegressionHelper(run_algo)
    out = reg_alys.regression()
    print(out)



    # plt.figure()
    # plt.plot(lst_size, lst_time, color='red')
    # plt.plot(lst_size, out['pred'], color='blue')
    # plt.legend(["GroundTurth", out['type']])
    # plt.show()
    # print(f"Cost is {out['cost']}\nParam is {out['param']}")
