def integral_value(low_val, high_val, pow):
    """ This function calculates the area under a curve """
    low_val_int = (low_val ** (pow + 1)) / (pow + 1)
    high_val_int = (high_val ** (pow + 1)) / (pow + 1)
    total_val = high_val_int - low_val_int
    return total_val


print("This program takes in a power of x for a simple integral, \
a low value of x, and a high value of x for a range of x, and")
print("calculates the area under the curve of x.")

p_x_index = 1
l_x_index = 1
u_x_index = 1

while True:
    try:
        power_of_x = int(input("What is the power of x in the integral? "))
    except ValueError:
        print("You must enter an integer. ")
        p_x_index += 1
        continue
    else:
        if p_x_index == 2:
            print("It's about time you entered an integer.")
        elif p_x_index == 3:
            print("Took you long enough.")
        elif p_x_index > 3:
            print("Wow, finally!")
        break

while True:
    try:
        lower_x_value = int(input("What is the lower value of x? "))
    except ValueError:
        print("You must enter an integer. ")
        l_x_index += 1
        continue
    else:
        if l_x_index == 2:
            print("It's about time you entered an integer.")
        elif l_x_index == 3:
            print("Took you long enough.")
        elif l_x_index > 3:
            print("Wow, finally!")
        break

while True:
    try:
        upper_x_value = int(input("What is the upper value of x? "))
    except ValueError:
        print("You must enter an integer. ")
        u_x_index += 1
    if upper_x_value <= lower_x_value:
        print("The upper x value must be greater than the lower x value.")
        continue
    else:
        if u_x_index == 2:
            print("It's about time you entered an integer.")
        elif u_x_index == 3:
            print("Took long enough.")
        elif u_x_index > 3:
            print("Wow, finally!")
        break

overall_value = integral_value(low_val=lower_x_value, high_val=upper_x_value,
                               pow=power_of_x)

print("The total value of the integral is " + str(round(overall_value, 2)) +
      " square units.")
