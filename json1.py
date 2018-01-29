import json
list1 = [1,2,3,4,5, 'qkl']
with open('file_json_dump.json', 'w') as file_object:
	json.dump(list1, file_object)

with open('file_json_dump.json', 'r') as file_object:
	tmpList1 = json.load(file_object)
	print(tmpList1)
