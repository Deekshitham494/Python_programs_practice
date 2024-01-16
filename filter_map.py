"""
Map:
synatx:  map(func, iterable)
* Map function returns list
"""

def str_upp(str):
    return str.upper()
names = ["alex", "John", "Bob", "william"]
upper_names = list(map(str_upp, names))
print(upper_names)

def sq_rt(num):
    return num**2
lst_a = [1, 2, 3, 4, 5]
sq_rts = list(map(sq_rt, lst_a))
print(sq_rts)

"""
Filter: Filter returns boolean values like False and True
filter(func, iterable)
"""
def palindrome_seq(word):
    if word==word[::-1]:
        return word

lst_words = ["bob", "alex", "malayalam"]
filt_pal = list(filter(palindrome_seq, lst_words))
print(filt_pal)

def hig_val(i):
    return i>75
scores = [67, 89, 85]
print(list(filter(hig_val, scores)))

from functools import reduce

def summation(x,y):
    return x+y

num = [1, 2, 3, 4, 5]
res = reduce(summation, num)
print(res)
