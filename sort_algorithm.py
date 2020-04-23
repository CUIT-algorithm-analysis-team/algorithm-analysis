from dataset import *
def select_sort(data):
    d1 = []
    while len(data):
        min = [0, data[0]]
        for i in range(len(data)):
            if min[1] > data[i]:
                min = [i, data[i]]
        del data[min[0]]  # 找到剩余部分的最小值，并且从原数组中删除
        d1.append(min[1])  # 在新数组中添加
    return d1

def bubble_sort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range (0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
    return lst

if __name__ == '__main__':
    for l in dataset.load_data(5):
        print(select_sort(l))