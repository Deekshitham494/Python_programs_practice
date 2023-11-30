lst_a = ["a", "b", [1, 2, 3, ["python"]]]
lst_a[2][3][0] = lst_a[2][3][0][::-1]
print(lst_a)

lst = [1, 2, 3, 7, 8, 6]
lst[3] = 10
print(lst)