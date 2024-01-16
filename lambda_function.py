"""
What is Lambda?
A Lambda function is a small anonymous function.
It can have any umber of arguments, but can only have one expression
"""

x = lambda a: a+20
print("The value of lambda expression is {}".format(x(10)))

y = lambda a, b: a+b
print("The value of lambda expression is {}".format(y(5, 9)))

s = lambda string: string.upper()
print("The upper case of string is {}".format(s("wElcOme")))

max_num = lambda a, b: a if a>b else b
print("The maximum value is {}".format(max_num(10,15)))

even_num = lambda x: [i for i in x if i%2==0]
print("The even numbers are {}".format(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])))