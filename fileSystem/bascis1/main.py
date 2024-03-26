# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# w - writing
# with open("my_file.txt", mode='w') as file:
#     file.write("New Text.")

# a - append
# with open("my_file.txt", mode='a') as file:
#     file.write("\nNew Text.")

# opening a file in write mode that dosent exist will be created, works only in write mode
# with open("new_file.txt", mode='w') as file:
#     file.write("New Text.")

# to open a file from desktop location
# with open("/Users/Shashank Tripathi/Desktop/fileSys.txt", mode='a') as file:
#     file.write("\nhey its working")

with open("../../../../../ShashankTripathi/Desktop/fileSys.txt", mode='a') as file:
    file.write("\nhey its working")