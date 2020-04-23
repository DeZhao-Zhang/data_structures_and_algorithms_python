class CircularQueue:

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
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """
        返回队列的第一个元素
        :return:
        """
        if self.is_empty():
            raise self.Empty("Queue is empty!")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        删除队列的第一个元素 并返回
        :return:
        """
        if self.is_empty():
            raise self.Empty("Queue is empty!")
        head = self._tail._next
        answer = head._element
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._tail._next = head._next
        return answer

    def enqueue(self, e):
        """
        入队列
        :param e:
        :return:
        """
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            head = self._tail._next
            newest._next = head
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """
        对队列的第一个元素进行出队和入队的操作
        :return:
        """
        if self._size > 0:
            self._tail = self._tail._next







