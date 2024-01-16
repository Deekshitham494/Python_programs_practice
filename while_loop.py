n=6
count = 0
while count<=n:
    print(count)
    count = count+1

# sum from 1 to 10
ini_val = 1
final_val = 10
sum = 0
while ini_val<=final_val:
    sum = sum+ini_val
    ini_val +=1
print("The sum of values from 1 to 10 is {}".format(sum))

# n!
n=10
count = 1
res = 1
while count<=n:
    res = res*count
    count +=1
print("The factorial value of n is {}".format(res))

# list out even and odd numbers from 1 to 10
n= 10
count= 1
evn_lst = []
odd_lst = []
while count<=n:
    if count%2==0:
        evn_lst.append(count)
    else:
        odd_lst.append(count)
    count+=1
print("The even list is {} and odd list is {}".format(evn_lst, odd_lst))

lst_a = [1, 2, 3, 4, 5]
lst_b = [6, 7, 8, 9, 10]
count = 0
res = []
if len(lst_a)==len(lst_b):
    while count<len(lst_b):
        res.append(lst_b[count]+lst_a[count])
        count+=1
print("the sum of lists are {}".format(res))