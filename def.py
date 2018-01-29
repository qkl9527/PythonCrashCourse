def func():
	print('func test')

func()

def func2(param1, param2='qkl'):
	print(param1 + 'hello ' + param2)

func2('start')
func2('start', 'zgq')
func2(param2='zgq', param1='start')

def func3(param1, *param):
	print(param1)
	print(param)


func3('qkl', 1,2,3,4)

def func4(param1, *param2, **param3):
	print(param1)
	print(param2)
	print(param3)

func4('qkl', 1,2,3,4, k='k1', k2='k2')