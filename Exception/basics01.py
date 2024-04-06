# basics

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"Key {error_msg} is not present")
else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")