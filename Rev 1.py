#Leon Oram
#27-01-2015
#Revision 1

class student:
    def __init__(self):
        self.name = ""
        self.mark = 0

def get_student():
    students=[]
    for count in range(3):
        new_student = student()
        new_student.name=input("Please enter student name: ")
        new_student.mark = int(input("Please enter the students mark: "))
        students.append(new_student)
    return students

students = get_student()
print("Student Name|Student Mark")
for count in range(3):
    print("{0:<12}|{1:^12}".format(students[count].name,students[count].mark))
