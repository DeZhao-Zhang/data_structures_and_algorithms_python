from ArrayStack import ArrayStack


class ReverseFile:

    def __init__(self):
        # 初始化一个栈对象
        self.data_stack = ArrayStack()

    def read_file(self, filename):
        # 读入文本文件
        original = open(filename)
        for line in original:
            self.data_stack.push(line.strip("\n"))
        original.close
    
    def reverse_data(self, filename):
        # 将栈中的元素逐个输出
        output = open(filename, "w")
        while not self.data_stack.is_empty():
            output.write(self.data_stack.pop() + "\n")
        output.close



if __name__ == "__main__":
    my_reverse = ReverseFile()
    my_reverse.read_file(r"D:\learning\数据结构与算法\Code\data_structures_and_algorithms_python\第六章 栈、队列和双端队列\reverse_file.txt")
    print(my_reverse.data_stack._data)
    my_reverse.reverse_data(r"D:\learning\数据结构与算法\Code\data_structures_and_algorithms_python\第六章 栈、队列和双端队列\test.txt")
