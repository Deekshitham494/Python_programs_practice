

try:
    s = "xyz"
    print(a)
except Exception as e:
    print(e)
#
# s = "xyz"
# print(a)


try:
    s = "xyz"
    print(a)
except Exception as e:
    print(e)
finally:
    print(s)

try:
    z = "abc"
    print(z)
except Exception as e:
    print(e)
finally:                                    # this will execute even though errors are raised
    print("The final code")

try:
    z = "abc"
    print(z)
except Exception as e:
    print(e)
else:                                   # this will execute only when try block is executed
    print("The else code")

try:
    s = "xyz"
    print(a)
except Exception as e:
    print(e)
else:
    print(s)


x = -1
if x<0:
    raise Exception("no numbers below zero")

x= "python"
if type(x) is not int:
    raise TypeError("Only integers are allowed")