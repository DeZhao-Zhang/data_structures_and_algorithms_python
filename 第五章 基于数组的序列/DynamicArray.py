import ctypes

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


if __name__ == "__main__":
    dynamaicArray = DynamicArray()
    
    n = 10  
    for k in range(n):
        # 获得data的长度
        a = dynamaicArray.__len__()
        # 获得data所占用的字节数
        b = dynamaicArray.get_capacity()
        # 打印
        print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
        # 给data增加一个元素
        dynamaicArray.append(None)