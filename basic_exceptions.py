# You can raise an exception to deal with errors

# sup_char_file = open("sup-char.csv")  # first raise FileNotFoundError

# deal with FileNotFoundError

try:
    sup_char_file = open("sup-char.csv")
    for line in sup_char_file:
        print(line)
except FileNotFoundError:
    print("The file doesn't seem to exist.")
    print("You Idjit.")
except Exception as e:
    print(e)
    print("You Idjit.")
finally:
    print("Even if your code works, you still have a lot to learn.")

