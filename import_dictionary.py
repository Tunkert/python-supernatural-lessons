import csv
sum = 0
n = 0

with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    grades_dict = {rows[0]: rows[1] for rows in reader}

with open("grades.txt", "a", encoding="utf-8") as text_file:
    for key, value in grades_dict.items():
        text_file.write(key + ": " + value)
        text_file.write("\n")
        if value != "Grade":
            sum += int(value)
        n += 1
    average = sum / n
    text_file.write("Class average: " + str(round(average, 2)))
