import random
print("Odd numbers")
counter = 0
while counter < 10:
    number = random.randint(1, 999)
    if int(number / 2) == number / 2:
        continue
    print(number)
    counter += 1
print("Loop is all done.")
