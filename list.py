list1 = ['qkl', 'zgq', 'pcb', 'nice']
print(list1)
print(list1[0])
print(list1[-1])
list1[0] = 'first'
list1.append('new');
list1.insert(0, 'insertFirst');
list1.insert(1, 'insertSecond');
print(list1)
lastItem = list1.pop()
print(lastItem)
print(list1)

#pop可指定index删除
index2Item = list1.pop(2)
print(index2Item)
print(list1)

#指定值删除
zgqItem = list1.remove('zgq')
print(zgqItem)
print(list1)

#用变量指定值删除
pcb = 'pcb'
pcbItem = list1.remove(pcb)
print(pcbItem)
print(list1)


#sort 按ascii码排序，一次取对比
list1.sort()
print(list1)

#sort 倒序排序
list1.sort(reverse=True)
print(list1)

# sortd 方式排序 不改变原有list1
print(sorted(list1))
print(list1)


# reverse 倒序排序
list1.reverse()
print(list1)




