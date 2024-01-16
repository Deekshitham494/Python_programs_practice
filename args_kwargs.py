"""
What is *args?
Basically *args are non-key worded arguments. It is represented using *. Many number of non-key worded arguments
can be passed using *args.
"Hello", "John"

What is **kwargs?
Basically **kwargs are key worded arguments. It is represented using **. Many number of key worded arguments
can be passed using **kwargs.
a= "1", b= "2"
"""

def arguments(*args):
    print(args)

arguments("Hello", "John", [1, 2, 4], "age")

def kwargs_ex(**kwargs):
    print(kwargs)
kwargs_ex(name= "John", age= "20", salary = "10000")

def print_args(*args):
    for i in args:
        print(i)
print_args("Hello", "John", [1, 2, 4], "age")

def print_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print_kwargs(name= "John", age= "20", salary = "10000")