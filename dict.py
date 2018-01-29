dict1 = {
	'name' : 'wc',
	'age' : 18
}

print(dict1)

print(dict1['name'])
print(dict1['age'])

dict1['tall'] = 180
dict1['company'] = 'sxx'

print(dict1)

for k, v in dict1.items():
	print(k)
	print(v)


print(dict1.keys())
print(dict1.values())
print(dict1.items())

