# Problem:
# Create a class called Student with the following:

# Attributes: name, grades (a list of grades).
# Methods:
# add_grade(grade) to add a grade to the grades list.
# average_grade() to calculate and return the average of the grades.
# Create an object of the Student class for "Emma". Add grades 85, 90, and 78 using the add_grade() method, and print Emma's average grade.

class Student:
    def __init__(self,name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grade = grade
        self.grades.append(self.grade)
    
    def avg_grade(self):
        sum = 0
        for marks in self.grades:
            sum += marks
        
        avg = sum / len(self.grades)

        return f"The Average Grade: {avg}"


Sname = input("Please Enter the name of Student: ")
grdlis = [12, 14, 23]
s1 = Student(Sname, grdlis)

gradesnum = int(input("Number of grades you want to Enter: "))

for itr in range(1, gradesnum+1):
    num = int(input(f"Enter the Grade{itr}: "))
    s1.add_grade(num)
    gradesnum -=1

print(s1.avg_grade())
