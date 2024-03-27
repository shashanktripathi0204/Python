# TODO: using list comprehension find the common int in both files
with open("file1.txt") as file1:
    file_one = file1.readlines()
file_one = [file.strip() for file in file_one]


with open("file2.txt") as file2:
    file_two = file2.readlines()
file_two = [file.strip() for file in file_two]

common_val = [int(num) for num in file_one if num in file_two]
print(common_val)