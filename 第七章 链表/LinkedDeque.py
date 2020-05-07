class _DoublyLinkedBase:
    """
    双向链表的基本类
    """

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)     # 头哨兵
        self._trailer = self._Node(None, None, None)    # 尾哨兵
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        在两个节点中间插入元素
        :param e: 插入元素
        :param predecessor: 前一个节点
        :param successor: 后一个节点
        :return:
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        删除一个节点
        :param node: 待删除的节点
        :return: 被删除节点的元素
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return element


class Empty(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        """
        :return: 队列的第一个元素
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """
        :return: 队列的最后一个元素
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        在队列的头部插入元素
        :param e: 插入的元素
        :return:
        """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        在队列的尾部插入元素
        :param e: 插入的元素
        :return:
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        删除队列的头部元素
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._header._next)

    def delete_last(self):
        """
        删除队列的尾部元素
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        self._delete_node(self._trailer._prev)