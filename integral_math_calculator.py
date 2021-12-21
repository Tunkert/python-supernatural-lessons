def integral_value(low_val, high_val, pow):
    """ This function calculates the area under a curve """
    low_val_int = (low_val ** (pow + 1)) / (pow + 1)
    high_val_int = (high_val ** (pow + 1)) / (pow + 1)
    total_val = high_val_int - low_val_int
    return total_val


print("This program takes in a power of x for a simple integral, \
a low value of x, and a high value of x for a range of x, and")
print("calculates the area under the curve of x.")


while True:
    try:
        power_of_x = int(input("What is the power of x in the integral? "))
    except ValueError:
        print("You must enter an integer. ")
        continue
    else:
        break

while True:
    try:
        lower_x_value = int(input("What is the lower value of x? "))
    except ValueError:
        print("You must enter an integer. ")
        continue
    else:
        break

while True:
    try:
        upper_x_value = int(input("What is the upper value of x? "))
    except ValueError:
        print("You must enter an integer. ")
    else:
        break

overall_value = integral_value(low_val=lower_x_value, high_val=upper_x_value,
                               pow=power_of_x)

print("The total value of the integral is " + str(round(overall_value, 2)) +
      " square units.")
