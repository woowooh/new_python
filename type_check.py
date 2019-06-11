class List(list):
	pass


# Function annotations， 方便 IDE 检测，和给看代码的人提示 
def return_type_check():
	def add(a: int, b: int)->int:
		return "1" # raise error
	c = add(1, 2)	
	c = add_return_str(1, 2)	
		# return a + b


def add_return_str(a: int, b: int)->int:
	return 1

# 类型检测，不同会报错，-> 提示返回类型，但不强制要求。。
def add(a: int, b: int):
	return a + b

# 同上
def add_list(a: List, b: int):
	length = len(a)
	for i in range(length):
		a[i] += b


def test_wrong_type():
	string_a = 1
	int_b = 2
	list_a = List([1, 2, 3, 4, 5])
	add(string_a, '1')	
	add_list(list_a, "3")


def test_normail_add():
	int_a = 1
	int_b = 2
	list_a = List([1, 2, 3, 4, 5])
	c = add(int_a, int_b)	
	add_list(list_a, int_b)
	print("add result is ", c)
	print(list_a)

def _main():
	return_type_check()
	test_normail_add()
	test_wrong_type()


_main()
