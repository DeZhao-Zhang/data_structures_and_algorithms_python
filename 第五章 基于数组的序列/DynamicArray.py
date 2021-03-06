import ctypes
from time import time


class DynamicArray:
    # 用于描述动态数组的类
    # 创建空数组
    # 获得数组的长度
    # 获得数组包含元素的数量
    # 添加元素

    def __init__(self):
        # 创建一个空数组
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        # 返回矩阵中保存的元素数目
        return self._n
    
    def get_capacity(self):
        # 获得矩阵的容量
        return self._capacity

    def __getitem__(self, k):
        # 获得矩阵的第k个元素
        if not 1<=k<self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        # 添加元素
        if self._n == self._capacity:
            self._resize(2*self._capacity);
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        # 对矩阵进行扩容
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        # 返回新的矩阵
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        # 在位置k处 插入值 value

        # 判断容量大小是否足够
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        # 将第n到第k个元素前移一位
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        # 插入值
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        # 移出列表中第一个出现的value
        for k in range(self._n):
            if self._A[k] == value:     # 找到匹配项
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]   # 前移一位
                self._A[self._n - 1] = None  # 方便垃圾回收
                self._n -= 1
                return  # 退出函数
        raise ValueError('value not found')

if __name__ == "__main__":
    dynamaicArray = DynamicArray()
    
    # # 测试动态列表对空间的获取特性
    # n = 10  
    # for k in range(n):
    #     # 获得data的长度
    #     a = dynamaicArray.__len__()
    #     # 获得data所占用的字节数
    #     b = dynamaicArray.get_capacity()
    #     # 打印
    #     print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
    #     # 给data增加一个元素
    #     dynamaicArray.append(None)

    # # 测试insert函数在插入不同位置时的效率
    # start = time()
    # for N in [100, 1000, 10000]:
    #     for num in range(N):
    #         # 分别测试k=0/k=num//2/k=num三种情况
    #         k = num
    #         dynamaicArray.insert(k, None)
    #     stop = time()
    #     print((stop - start)/N)