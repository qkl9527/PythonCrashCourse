# 触发不能为0错误捕获
try:
	5 / 0
except ZeroDivisionError:
	print('zeor error')

# 文件不存在错误
# with open("filenotexist.txt") as file_object:
	# print(file_object.read())

list1 = "q k l k    3 4 5 @ 45".split()
print(list1)
countLen = len(list1)
print(countLen)

