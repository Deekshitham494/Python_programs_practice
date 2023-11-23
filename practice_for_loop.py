str_a = "hello"
for i in str_a:
    print(i)

lst_a = ["a", "b", "c", "d"]
for i in lst_a:
    print(i)

tpl_a = ("e", "f", "g")
for i in tpl_a:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    print(i)
for i in str_y:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    for j in str_y:
        print((i,j))


