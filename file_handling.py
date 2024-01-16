# File reading outside the path

out_file_path = "C://Users//deeks//OneDrive//Documents//file_read.txt"
file_open = open(out_file_path, "r")
read_file = file_open.read()
print(read_file)
# for each in file_open:
#     print(each)

# File reading inside the path
inside_file_path = "file_read.txt"
with open(inside_file_path, "r") as file:
    data = file.read()
print(data)

with open("sample.txt", "w") as f:
    f.write("welcome to python class"+"\n")
    f.write("John is clever"+"\n")

file = open("sample_to_write.txt", "w")
file.write("John holds an offer")
file.close()