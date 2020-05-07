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


class PositionalList(_DoublyLinkedBase):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """
        判断位置节点是否有效
        :param p: 给出的位置节点
        :return: 位置节点的node
        """
        if not isinstance(p, self.Position):    # 判断节点是否为位置节点
            raise TypeError("p must be proper Position type")
        if p._container is not self:    # 判断该位置节点是否属于该链表
            raise ValueError("p does not belong to this container")
        if p._node._next is None:   # 判断该位置节点的node是否有效
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """
        创建位置节点
        :param node: 需要包装成位置节点的Node
        :return: 位置节点
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """
        返回第一个节点的位置节点
        :return:
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        返回最后一个节点的位置节点
        :return:
        """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        返回p位置节点前的位置节点
        :param p: 位置节点p
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        返回位置节点p后面的位置节点
        :param p: 位置节点p
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """
        在两个节点之间插入元素
        :param e: 需要插入的元素
        :param predecessor: 插入的前节点
        :param successor: 插入的后节点
        :return: 返回新的位置节点
        """
        node = super()._insert_between(e, predecessor, successor)   # 插入元素 获得节点
        return self._make_position(node)

    def add_first(self, e):
        """
        在头部增添元素
        :param e:
        :return:
        """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """
        在尾部增添元素
        :param e:
        :return:
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        在位置节点p前添加元素e
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """
        在位置节点p后添加元素e
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """
        删除位置节点p
        :param p:
        :return:
        """
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """
        更换位置节点p的元素
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

