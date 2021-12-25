import csv

grades_dict = {}

with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    grades_dict = {rows[0]: rows[1] for rows in reader}

print(grades_dict)
