# 写，w表示存在的内容会被重写
with open('file2.txt', 'w') as file_object:
    file_object.write("hello python3!\n")
    file_object.write("hello python3!\n")
    file_object.write("hello python3!\n")
    file_object.write("hello python3!\n")

# 写，a表示现在有内容后新增
with open('file2.txt', 'a') as file_object:
    file_object.write("hello python3 append!\n")
    file_object.write("hello python3 append!\n")
    file_object.write("hello python3 append!\n")
    file_object.write("hello python3 append!\n")

