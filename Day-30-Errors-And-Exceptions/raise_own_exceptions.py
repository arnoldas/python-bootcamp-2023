height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3: #height more than 3 meters
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
