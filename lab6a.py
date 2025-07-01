#!/usr/bin/env python3
# Author ID: mjndolla-wafo

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = str(name)       # Fix 1: convert number to string to avoid TypeError
        self.number = str(number)   # Fix 1: convert number to string to avoid TypeError
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'  # Fix 2: handle ZeroDivisionError
        gpa = sum(self.courses.values()) / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Return a list of course that the student passed (not a 0.0 grade)
    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', 123456)  # Accepts int due to fix
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display student1 info
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display student2 info
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
