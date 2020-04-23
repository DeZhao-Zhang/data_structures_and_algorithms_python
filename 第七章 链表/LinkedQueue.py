class LinkedQueue:

    """使用单链表实现队列 链表头部作为队列的头(出数据)  链表尾部作为队列的尾(入数据)"""

    class _Node:
        """
        用于保存一个链表节点
        """
        __slots__ = "_element", '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    class Empty(Exception):
        pass

    def __init__(self):
        """
        队列的初始化
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        返回队列的长度
        :return: 队列的长度
        """
        return self._size

    def is_empty(self):
        """
        判断队列是否为空
        :return: true or false
        """
        return self._size == 0

    def first(self):
        """
        获得队列头部元素的值
        :return:
        """
        if self.is_empty():
            raise self.Empty("Queue is empty!")
        return self._head._element

    def dequeue(self):
        """
        出队列操作
        :return: 返回队列头部的值
        """
        if self.is_empty():
            raise self.Empty("Queue is empty!")

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None  # 如果此时队列为空  则将队列的尾部赋值None
        return answer

    def enqueue(self, e):
        """
        队列入队列操作
        :param e:
        :return:
        """
        newest = self._Node(e, None)    # 生成节点
        if self.is_empty():     # 如果队列为空  则队列头部也指向最新节点
            self._head = newest
        else:       # 如果队列非空  则只将旧的队尾节点next指向最新节点
            self._tail._next = newest
        self._tail = newest     # 更新队尾节点

        self._size += 1


if __name__ == "__main__":
    queue = LinkedQueue()
    print(queue._head, queue._tail)
    queue.enqueue(1)
    print(queue._head, queue._tail)
    print(queue.__len__())
    queue.enqueue(2)
    queue.enqueue(5)
    print(queue.__len__())
    print(queue.first())
    print("len after first is {}".format(queue.__len__()))
    print(queue.dequeue())
    print("len after first dequeue is {}".format(queue.__len__()))
    print(queue.dequeue())
    print("len after second dequeue is {}".format(queue.__len__()))
    print(queue.dequeue())
    print("len after third dequeue is {}".format(queue.__len__()))
    print(queue._head, queue._tail)
    # print(queue.dequeue())


