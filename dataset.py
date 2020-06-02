from random import shuffle

class dataset():
    def __init__(self):
        """
        :param n:数据的规模
        """
        self.datapath = "data"
    @staticmethod
    def load_data(n, start=1, step=1):
        '''
        直接把乱序数据输出去
        :param n: n 数据规模
        :param start: 起始规模
        :param step: 步长
        :return:
        '''
        for i in range(start, n+1, step):
            l = [j for j in range(i)]
            shuffle(l)
            yield l

    @staticmethod
    def load_order_data(n, start=1, step=1):
        '''
        返回顺序的数据
        :param n: n 数据规模
        :return:
        '''
        for i in range(start, n + 1, step):
            l = [j for j in range(i)]
            yield l

    @staticmethod
    def load_reorder_data(n, start=1, step=1):
        '''
        返回逆序的数据
        :param n: n 数据规模
        :return:
        '''
        for i in range(start, n + 1, step):
            l = [j for j in range(i)].reverse()
            yield l

if __name__ == '__main__':
    for l in dataset.load_data(4000, 100, 100):
        print(l)
    print("finish")


