print(sum(i for i in range(1, 101)))

counter = 0


def increment_counter():
    global counter
    counter += 1;


increment_counter()

print(counter)
# os模块：提供与操作系统交互的函数，如访问文件系统、创建文件夹等。
#  sys模块：提供与Python解释器交互的函数，如访问命令行参数、退出程序等。
# re模块：提供正则表达式相关的函数，用于匹配和处理文本数据。
# json模块：处理JSON格式数据，如将JSON解析为Python对象。
# datetime模块：处理日期和时间，如创建日期时间对象、获取当前日期时间等。
# argparse模块：处理命令行参数，用于编写命令行应用程序。
# collections模块：提供有用的数据结构和函数，如Counter、OrderedDict等。
# random模块：生成随机数，如随机整数、随机浮点数等。
# itertools模块：提供与迭代器相关的函数，如无限迭代器、组合迭代器等。
# logging模块：提供日志记录相关的函数，用于跟踪程序运行时的信息、错误等。

# 05
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)

print(dict1)

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
#
# merged_dict = {==&zwnj;**dict1, **&zwnj;==dict2}
#
# print(merged_dict)

# 方法3: 使用.copy()和update()

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {k: v for d in [dict1, dict2] for k, v in d.items()}

print(merged_dict)

# 在Python中，大多数标准类型（除了字典类型之外）确实都可以直接用于布尔测试，这意味着它们可以在布尔上下文中被评估为 True 或 False。这通常是通过检查它们是否为空或是否包含某些元素来实现的。
#
# 以下是一些标准类型及其在布尔测试中的行为：
#
# ‌字符串‌：
#
# 空字符串 "" 被评估为 False。
# 非空字符串被评估为 True。
# ‌列表‌：
#
# 空列表 [] 被评估为 False。
# 非空列表被评估为 True。
# ‌元组‌：
#
# 空元组 () 被评估为 False。
# 非空元组被评估为 True。
# ‌集合‌：
#
# 空集合 set() 被评估为 False。
# 非空集合被评估为 True。
# ‌冻结集合（frozenset）‌：
#
# 空冻结集合 frozenset() 被评估为 False。
# 非空冻结集合被评估为 True。
# ‌数字类型‌（如整数、浮点数、复数）：
#
# 数字 0 被评估为 False。
# 任何非零数字被评估为 True。
# ‌布尔类型‌：
#
# False 值本身就是 False。
# True 值本身就是 True。
# ‌NoneType‌：
#
# None 被评估为 False。
# 然而，字典类型在布尔测试中有其特殊的行为：
#
# 在Python 3.7及更高版本中，直接对字典进行布尔测试会检查它是否为空。空字典 {} 被评估为 False，非空字典被评估为 True。
# 在Python 3.6及更早版本中，直接对字典进行布尔测试是不允许的，并且会引发 TypeError。但这一行为在Python 3.7中已经被改变，以使其与其他容器类型保持一致。
# 因此，可以说在Python 3.7及更高版本中，‌所有‌标准类型（包括字典）都可以用于布尔测试。而在更早的Python版本中，字典需要特别处理（例如通过检查其长度 len(dict) 来确定是否为空）。
#
# 这里是一些示例代码：
#
# python
# Copy Code
# Python 3.7+
print(bool(""))       # False
print(bool([]))       # False
# print(bool(()))       # False
# print(bool(set()))    # False
# print(bool(frozenset())) # False
# print(bool(0))        # False
# print(bool(1))        # True
# print(bool(False))    # False
# print(bool(True))     # True
# print(bool(None))     # False
# print(bool({}))       # False
# print(bool({"a": 1})) # True

print(0 or False and 1)

x=y=z=1
# x=(y=z+1)

# a = (1,2,3,4)
# a[0] = 2
# print(a)

a = [1,2,3]
b=[3,4]
a.append(b)
print(len(a))
# print(sum(a))
print(a[-1])

a = [1,2,3,4]
b = [3,4,[5,6]]

a.append(b) # [1,2,3,4, [3,4,[5,6]]]
a.extend(b) # [1,2,3,4, [3,4,[5,6]], [3,4,[5,6]]]
a = a + b # [1,2,3,4, [3,4,[5,6]], 3,4,[5,6], 3,4,[5,6]]

a.pop(1)
# a.remove(2)
print(a)


for n in 'abcd':
    print(n)

for n in (3,4,5):
    print(n)

b = [1,2,3]
def ccc(c):
    c.append(4)
ccc(b)
print(b)
def bb(b):
    b=5
bb(b)
print(b)
a = [1,2]
m = [1,2]
print(a is m)
print(a == m)
n = a
print(n is a)
x=1
y=2

m_list = [1,2,3,4,5,1,2,3]
s = set()
l = [x for x in m_list if x not in s and not s.add(x)]
print(l)

original_list = [1, 2, 3, 4, 5, 4, 3]
seen = set()
unique_list = [x for x in original_list if x not in seen and not seen.add(x)]
print(unique_list)  # 输出 [1, 2, 3, 4, 5]

import copy
a = [1,2,3,4]
b = copy.copy(a)
print(id(a[1]) == id(b[1]))

class h():
    def showInfo(self):
        print(self.x)

ah  = h()
ah.showInfo()