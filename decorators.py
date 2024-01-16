"""
What is decorators?
Decorators allow us to wrap another function in order to extend the behaviour of wrapped function
without permanently modifying it.
                                    or
Decorators changes the behaviour of existing function during runtime.
Decorate using @
"""

def sqr_num(func):
    def wrapper():
        x = func()
        sqr = x**2
        return sqr
    return wrapper

@sqr_num
def number():
    return 10

print(number())


def acceleration(func):
    def inner_method(*args, **kwargs):
        vel = func(*args, **kwargs)
        time = args[1]
        acce = vel/time
        return acce
    return inner_method
@acceleration
def velocity(dis, time):
    vel = dis/time
    return vel
print(velocity(100, 60))


def mult_three(func):
    def wrapper(*args, **kwargs):
        summ = func(*args, **kwargs)
        res = summ*3
        return res
    return wrapper
@mult_three
def summation(a, b, c=2, d= 4):
    sum_abcd = a+b+c+d
    return sum_abcd
print(summation(5,7, c= 5, d=10))