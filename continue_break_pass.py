# break

fruits = ["apple", "orange", "banana", "grapes", "mango"]
for i in fruits:
    print(i)
    if i == "banana":
        print("I found banana")
        break

count = 0
while count<12:
    print(count)
    if count == 8:
        print("end the program")
        break
    count += 1

# continue
fruits = ["apple", "orange", "banana", "grapes", "mango"]
for i in fruits:
    print(i)
    if i == "banana":
        print("I found banana")
        continue

count = 0
while count<12:
    print(count)
    count += 1
    if count == 8:
        print("end the program")
        continue

# pass
def num():
    pass
print(num())