list1 = ['qkl', 'zgq', 'pcb', 'nice']
print(list1)
for x in list1:
	print(x)

for y in range(1, 9):
	print(y)


print(list(range(1, 9)))
print(list(range(1, 9, 3)))

result = [];
for z in range(1,11):
	result.append(z**2)

result2 = [x**2 for x in range(1,11)]
print(result2)

print(result)

print(min(result))

print(max(result))

print(sum(result))

result3 = []
print(sum(range(1, 1000001)))

for x in range(3, 30):
	if x % 3 == 0:
		result3.append(x)

print(result3)