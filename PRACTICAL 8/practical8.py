# ID   : 20CE141
# NAME : PRATIK SUTHAR

"""Aim : Write a Program in Python to implement a Stack Data Structure
         using Class and Objects, with push, pop, and
         traversal method."""


class Stack:
    top = -1  # Assign index -1 to the top...
    stack = []  # Create empty stack

    def push(self, new_element):  # Method to push element into the stack
        self.stack.append(new_element)  # append data into the stack
        self.top += 1  # increment the value of top...
        print("Push Succeed")

    def pop(self):  # Method to pop out element from the stack
        if self.top < 0:  # If stack is empty, then value of top is -1 which is < 0.
            print("Underflow (Stack is empty)")
        else:
            self.stack.pop()  # If top >=0, then pop possible...
            self.top -= 1  # increment the value of top...
            print("Pop Succeed")  # Top element of stack will be pop out from the stack

    def traverse(self):  # Method for print All elements of the stack...
        i = self.top
        while i > -1:
            print(self.stack[i])
            i -= 1


o1 = Stack()  # Create object of stack class as a o1
while True:
    print('1. Push\n2. Traverse\n3. Pop\n4. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:  # Push Operation to push element into stack
        x = int(input('Enter Number to push : '))
        o1.push(x)  # push() method call
        print()

    elif choice == 2:  # Printing Data Using traverse function of stack class.
        o1.traverse()  # traverse() method call
        print()

    elif choice == 3:  # Pop Operation to pop element from stack
        o1.pop()  # pop() method call
        print()

    elif choice == 4:  # choice 4 for exit
        break

    else:
        print('Selected option is Invalid please Select valid option...')
        choice = int(input('Enter Your choice : '))
