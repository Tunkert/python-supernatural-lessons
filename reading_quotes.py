with open("supernatural-quotes.txt") as file:
    line = file.readline()
    i = 2
    while line:
        if i % 2 == 0:
            print(line)
        i += 1
        line = file.readline()
