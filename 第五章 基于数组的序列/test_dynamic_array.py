import sys
# list of test
data = []
# finally num of data
n = 10  
for k in range(n):
    # 获得data的长度
    a = len(data)
    # 获得data所占用的字节数
    b = sys.getsizeof(data)
    # 打印
    print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
    # 给data增加一个元素
    data.append(None)

