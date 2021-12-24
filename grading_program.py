import csv
user_continue = "y"
student_scores = []
student_list = []

while user_continue == "y":
    while True:
        try:
            student_name = input("Enter the name of the of the next student. ")
            student_grade = int(input("What is the grade of the student? "))
            student_list.append(student_name)
            student_list.append(student_grade)
            break
        except ValueError:
            print("You must enter an integer value for the grade. ")
            continue
    student_scores.append(student_list)
    student_list = []
    user_continue = (input("Do you want to enter another grade(y for yes,\
 n for no)? ")).lower()

header = ['Name', 'Grade']

grade_file = 'student_grades.csv'
with open(grade_file, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(student_scores)
