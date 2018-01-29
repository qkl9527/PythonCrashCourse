# 一次性全读取
with open('file1.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\n")

# 迭代每行
with open('file1.txt') as file_object:
    for line in file_object:
    		print(line.strip())

print("\n")

# 迭代每行
with open('file1.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
	print(line.strip())