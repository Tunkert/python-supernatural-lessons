scores = [88, 92, 78, 90, 98, 84]
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students[0])

students.insert(3, "Amber's friend")

for score in scores:
    print(score)

for student in students:
    if student == "Amber":
        print(student + "'s name starts with an A.")
    else:
        print(student)
