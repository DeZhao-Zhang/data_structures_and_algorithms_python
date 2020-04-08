import sys
from time import time


# 代码段5-1 验证python的列表使用动态数组技术
def verify_python_list_use_dynamic_array():
    # list of test
    data = []
    # finally num of data
    n = 10  
    for k in range(n):
        # 获得data的长度
        a = len(data)
        # 获得data所占用的字节数
        b = sys.getsizeof(data)
        # 打印
        print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
        # 给data增加一个元素
        data.append(None)


# 代码段5-4 测试python列表类增添操作的摊销花费
def compute_average(n):
        data = []
        start = time()
        for k in range(n):
                data.append(None)
        end = time()
        return (end - start) / n


# # 测试代码段5-1
# verify_python_list_use_dynamic_array()

# # 测试代码段5-4
# for i in range(4, 10):
#         n = 10**i
#         print(compute_average(n))