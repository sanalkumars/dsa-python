class stack:
    def __init__(self):
        self.stacklist =[]

    def stacklength(self):
        return len(self.stacklist)
    
    # function for adding an element to the stack
    def push(self,element):
        self.stacklist.append(element)
        print("Element added to the stack")

    # function for removing an element from the stack and printing the element removed
    def pop(self):
        if self.stacklength() == 0:
            print("Stack is empty || stack is in underflow condition")
        else:
            removed_element = self.stacklist.pop()
            print(f"Element removed from the stack: {removed_element}")

    # function for printing the top element of the stack
    def peek(self):
        if self.stacklength() == 0:
            print("Stack is empty || stack is in underflow condition")
        else:
            top_element = self.stacklist[-1]
            print(f"Top element of the stack: {top_element}")

    # function for printing the stack elements
    def printStack(self):
        if self.stacklength() == 0:
            print("Stack is empty || stack is in underflow condition")
        else:
            print("Stack elements:")
            for element in reversed(self.stacklist):
                print(element,"--")


newstack = stack()
newstack.push(10)
newstack.push(20)
newstack.push(30)
newstack.printStack()
newstack.pop()
newstack.peek()
newstack.printStack()