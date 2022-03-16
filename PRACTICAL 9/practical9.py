# ID   : 20CE141
# NAME : PRATIK SUTHAR


"""Aim :
   Consider an example of declaring the examination result.

   Design three classes: Student, Exam, and Result.
   The Student class has data members such as those representing rollNumber, Name, etc.

   Create the class Exam by inheriting Student class.
   The Exam class adds fields representing the marks scored in six subjects.

   Derive Result from the Exam class, and it has its own fields such as total_marks.

   Write an interactive program to model this relationship."""


class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name

    def display(self):
        print("\tStudent Data : ")
        print("\tRoll Number :", self.rollNumber)
        print("\tName :", self.name)


class Exam(Student):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name)
        self.mark = []
        for m in marks:
            self.mark.append(m)

    def display(self):
        super().display()
        n = 0
        for display_loop in self.mark:
            print("\tMark of subjects ", n + 1, "\b :", display_loop)
            n += 1


class Result(Exam):
    def __init__(self, rollNumber, name, marks):
        super().__init__(rollNumber, name, marks)
        self.total_marks = 0
        for mark in marks:
            self.total_marks += mark

    def display(self):
        super().display()
        print("\tTotal Marks : ", self.total_marks)


number_of_students = int(input("Enter number of students : "))
i = 0
obj = []  # create list name as a obj
while i < number_of_students:
    print("Enter details for student", i + 1)
    Name = input("\tEnter name of student : ")
    roll_number = input("\tEnter roll number of student : ")
    Marks = []  # create list name as a marks
    for j in range(6):
        print("\tEnter mark for subject", j + 1, "\b:- ", end='')
        Mark = int(input())
        Marks.append(Mark)  # add marks into Marks list
    obj.append(Result(roll_number, Name, Marks))
    print()
    i += 1

i = 0
while i < number_of_students:
    print("Result of student", i + 1)
    obj[i].display()
    print()
    i += 1