# raising user defined exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height is not above 3 meters")
bmi = weight / height ** 2
print(bmi)