answers = ["A", "B", "", "D", "E"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("The loop is done.")
