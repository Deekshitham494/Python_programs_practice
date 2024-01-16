def summation(a, b):
    sum_a_b = a+b
    return sum_a_b

sum_ab = summation(6, 7)
print("Th sum of a and b is {}".format(sum_ab))

def sum_diff(a,b):
    sum_ab = summation(a,b)
    diff = a-b
    return sum_ab, diff
print(sum_diff(14, 7))
res = sum_diff(18, 7)
print("The value of sum {} and diff {}".format(res[0], res[1]))