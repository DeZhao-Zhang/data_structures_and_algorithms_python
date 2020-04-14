from Empty import Empty

class ArrayQueue:
    # 使用Python的list作为底层构建循环式队列
    DEAFAULT_CAPACITY = 10 # 队列的默认容量

    def __init__(self):
        # 初始化一个空队列
        self._data = [None] * ArrayQueue.DEAFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        # 获得当前队列的长度
        return self._size

    def is_empty(self):
        # 判断队列是否为空
        return self._size == 0

    def first(self):
        # 返回队列的第一个值
        if self.is_empty():
            raise Empty("Queue is Empty")

        return self._data[self._front]

    def dequeue(self):
        # 删除并返回队列的第一个值
        if self.is_empty(): # 判断是否为空
            raise Empty("Queue is Empty")

        answer = self._data[self._front]    # 获得队列第一个值
        self._data[self._front] = None  # 将原先位置赋值None 利于垃圾回收
        self._front = (self._front + 1) % len(self._data)   # 更新self._front
        self._size -= 1 # 更新self._size
        if 0 < self._size < len(self._data) // 4:   # 如果当前元素小于数组大小的四分之一  则缩减数组
            self._resize(len(self._data) // 2)
        return answer   

    def enqueue(self, e):
        # 添加一个元素
        if self._size == len(self._data):   # 如果队列已满 则扩大队列
            self._data = self._resize(2 * len(self._data))
        avail = (self._front + self._size + 1) % len(self._data)
        self._data[avail] = e
        self._size += 1



    def _resize(self, cap):
        # 根据新的cap构建队列 并移动元素
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size): # 将队列的首部索引重新调整为0，并依次排入
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


if if __name__ == "__main__":
    # 疑问1： 此处使用列表来构建的话，当元素个数接近列表大小的时候  python本身不也会对它进行扩展吗
    # 疑问2： 使用动态数组的方式扩展容量 为什么还需要循环  因为可能大小没有超过 但是一直进出进出