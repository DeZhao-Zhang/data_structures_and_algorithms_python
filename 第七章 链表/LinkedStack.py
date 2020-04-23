class LinkedStack:

    """使用单链表实现栈"""

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
        栈的初始化
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """
        返回栈的长度
        :return: 栈的长度
        """
        return self._size

    def is_empty(self):
        """
        判断栈是否为空
        :return: true or false
        """
        return self._size == 0

    def push(self, e):
        """
        向栈中压入一个元素
        :param e: 元素的值
        :return:
        """

        self._head = self._Node(e, self._head)  # 创建节点
        self._size += 1

    def pop(self):
        """
        出栈 弹出栈顶元素
        :return: 栈顶节点的值
        """
        if self.is_empty():
            raise self.Empty('Stack is empty')
        answer = self._head._element    # 获得栈顶元素的值
        self._head = self._head._next   # 将栈顶移动一位
        self._size -= 1    # 将栈的大小减一
        return answer   # 返回栈顶元素的值

    def top(self):
        """
        返回栈顶元素
        :return:
        """
        if self.is_empty():
            raise self.Empty('Stack is empty')
        return self._head._element


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    print(stack.__len__())
    stack.push(2)
    stack.push(5)
    print(stack.__len__())
    print(stack.top())
    print("len after top is {}".format(stack.__len__()))
    print(stack.pop())
    print("len after first pop is {}".format(stack.__len__()))
    print(stack.pop())

