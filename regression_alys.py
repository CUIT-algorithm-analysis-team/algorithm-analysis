import numpy as np
from scipy.optimize import least_squares


def residuals_nlogn(param, y, x):
    a, b = param
    return y - (a * x * np.log(x) + b)


def residuals_n2(param, y, x):
    a, b = param
    return y - (a * np.power(x, 2) + b)


def regression(lst_time, lst_size):
    """
    Regression Analysis.
    :param lst_time: A list, cost time as Y axis.
    :param lst_size: A list, question size as X axis
    :return: A dict.{'type': str 'nlogn' or 'n2',
                     'cost': float,
                     'pred': list,
                     'param': tuple(a, b)  nlogn is (a*nlogn + b). n2 is  (a*n^2 + b)}
    """
    out = {}
    nlogn = least_squares(residuals_nlogn, [1, 1], args=(np.array(lst_time), np.array(lst_size)))
    n2 = least_squares(residuals_n2, [1, 1], args=(np.array(lst_time), np.array(lst_size)))

    if nlogn['cost'] < n2['cost']:
        pred_time_nlogn = nlogn['x'][0] * np.array(lst_size) * np.log(lst_size) + nlogn['x'][1]
        out['type'] = 'nlogn'
        out['cost'] = round(nlogn['cost'], 6)
        out['pred'] = pred_time_nlogn.tolist()
        out['param'] = (nlogn['x'][0], nlogn['x'][1])
    else:
        pred_time_n2 = n2['x'][0] * np.power(np.array(lst_size), 2) + n2['x'][1]
        out['type'] = 'n2'
        out['cost'] = round(n2['cost'], 6)
        out['pred'] = pred_time_n2.tolist()
        out['param'] = (n2['x'][0], n2['x'][1])

    return out


if __name__ == '__main__':
    from dataset import dataset
    from sort_algorithm import *
    import time
    import matplotlib.pyplot as plt

    data = dataset()
    lst_size = []
    lst_time = []

    for item in data.load_data(1000, 100, 100):
        start = time.time()
        bubble_sort(item)
        stop = time.time()
        lst_size.append(len(item))
        lst_time.append((stop-start))

    out = regression(lst_time, lst_size)
    plt.figure()
    plt.plot(lst_size, lst_time, color='red')
    plt.plot(lst_size, out['pred'], color='blue')
    plt.legend(["GroundTurth", out['type']])
    plt.show()
    print(f"Cost is {out['cost']}\nParam is {out['param']}")
