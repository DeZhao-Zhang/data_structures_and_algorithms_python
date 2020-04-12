from Empty import Empty


class ArrayStack:
    # 使用Python的list类来构建栈数据结构

    def __init__(self):
        # 创建空栈
        self._data = []

    def __len__(self):
        # 返回栈中元素的个数
        return len(self._data)

    def is_empty(self):
        # 判断是否为空
        return len(self._data) == 0

    def push(self, e):
        # 像栈顶添加元素e
        self._data.append(e)

    def top(self):
        # 返回栈顶元素
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        # 弹出并返回栈顶元素
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


if __name__ == "__main__":
    
    my_stack = ArrayStack()
    
    my_stack.push(5)
    print(my_stack._data)
    
    my_stack.push(3)
    print(my_stack._data)
    
    print(my_stack.__len__())

    my_stack.pop()
    print(my_stack._data)
   
    print(my_stack.is_empty())

    my_stack.top()
    print(my_stack._data)

    my_stack.pop()
    print(my_stack._data)

    print(my_stack.is_empty)

    my_stack.pop()

