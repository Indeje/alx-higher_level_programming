#!/usr/bin/python3

# 0-main
# lookup = __import__('0-lookup').lookup

# class MyClass1(object):
# 	pass

# class MyClass2(object):
# 	my_attr1 = 3
# 	def my_meth(self):
# 		pass

# print(lookup(MyClass1))
# print(lookup(MyClass2))
# print(lookup(int))


# 1-main
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
