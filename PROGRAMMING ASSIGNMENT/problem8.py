class Parent1:

    def show(self):
        print("Inside Parent Class 1")


class Parent2:

    def display(self):
        print("Inside Parent Class 2")


class Child(Parent1, Parent2):

    def show(self):
        print("Inside Child Class")


obj = Child()
obj.show()
obj.display()
