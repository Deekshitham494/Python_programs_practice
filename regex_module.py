import re

# Search

txt_a = "Its raining at my place"
x = re.search("raining", txt_a)
if x:
    print("Searched successfully")
else:
    print("No match")

y = re.search("^Its.*place$", txt_a)
if y:
    print("Yes, match is successful")
else:
    print("No, Match found")

# find all
txt_b = "The rain in spain"
a = re.findall("ai", txt_b)
print(a)
b = re.findall("in", txt_b)
print(b)

txt_c = "Its quater 8 in the morning"
z = re.findall("[a-zA-Z]", txt_c)
print(z)
y = re.findall("[0-9]",txt_c)
print(y)
b = re.findall("[1234]", txt_c)
if b:
    print("Pattern matched")
else:
    print("No matches found")