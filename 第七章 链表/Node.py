class _Node:

    """
    用于保存一个链表节点
    """
    __slots__ = "_element", '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next



