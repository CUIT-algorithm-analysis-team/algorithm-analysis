from random import shuffle

class dataset():
    def __init__(self):
        """
        :param n:数据的规模
        """
        self.datapath = "data"

    def create_dataset(self,n):
        """
        生成数据，保存到txt中，至于到底要不要保存到txt,还是直接生成,后面可以讨论
        :param n: n 个数量集合的数据。
        :return: 向文件中保存 固定格式的 txt
        """
        for i in range(1,n + 1):
            filename = self.datapath + "/" + str(i) + ".txt"
            with open(filename,'w') as f:
                l = [str(j) for j in range(i)]
                shuffle(l)
                sep = ','
                f.write(sep.join(l))
                f.close()

    def load_data(self,n):
        '''
        直接把数据输出去
        :param n: n 数据规模
        :return:
        '''
        for i in range(1,n + 1):
            l = [str(j) for j in range(i)]
            shuffle(l)
            yield l

if __name__ == '__main__':
    a = dataset()
    for l in a.load_data(1000):
        print(l)
    print("finish")


