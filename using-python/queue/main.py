# This is for implementing a queue using a list in Python.

class Queue:
    def __init__(self):
        self.queue=[]

    # funcation for adding an element to the queue
    def enqueue(self,value):
        self.queue.append(value)
    
    # function for removing an element from the queue and printing the element removed
    def dequeue(self):
        if len(self.queue) ==0:
            raise Exception("Queuse is Empty || Queue is in underflow condition")
        else:
            removed_element = self.queue.pop(0)
            print(f"Element removed from the queue: {removed_element}")
    # function for printing the front element of the queue
    def peek(self):
        if len(self.queue) ==0:
            raise Exception("Queuse is Empty || Queue is in underflow condition")
        else:
            print(f"Front element of the queue: {self.queue[0]}")

    def printQueue(self):
        if len(self.queue) ==0:
            raise Exception("Queuse is Empty || Queue is in underflow condition")
        else:
            print("Queue elements:")
            for element in self.queue:
                print(element,"--")

newqueue = Queue()
newqueue.enqueue(10)    
newqueue.enqueue(20)
newqueue.enqueue(30)
newqueue.printQueue()
newqueue.peek()
newqueue.dequeue()
newqueue.peek()
newqueue.printQueue()