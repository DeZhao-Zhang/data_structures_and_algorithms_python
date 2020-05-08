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


class FavoritesList:

    class _Item:
        __slots__ = '_value', "_count"

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        """
        遍历整个self._data 找到存储e的节点
        :param e:
        :return:
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():     # 如果已经是第一节点  则直接跳过
            cnt = p.element()._count    # 获得该节点元素的访问数量
            walk = self._data.before(p)
            if cnt > walk.element()._count:     # 如果被访问节点的访问数目已经超过前一个节点
                while (walk != self._data.first() and cnt > self._data.before(walk).element._count()):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))   # 删除旧节点 并重新插入

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)  # 找到e对应的节点
        if p is None:   # 如果该节点不存在 则创建该节点
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1     # 将该节点的访问数量加一
        self._move_up(e)    # 对该节点进行排序

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


class FavoritesListMTF(FavoritesList):

    def _move_up(self, p):
        if p != self._data.first()
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            high_pos = temp.first()
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element()._count > high_pos.element()._count():
                    high_pos = walk
                walk = temp.after(walk)
            yield high_pos.element()._value()
            temp.delete(high_pos)