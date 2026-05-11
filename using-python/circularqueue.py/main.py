

class circularQueue:
    def __init__(self , size=5):
        self.queue = [None] * size
        self.front =-1
        self.rear =-1
        self.count = 0

    def isFull(self):
        if self.count == len(self.queue):
            return True
        else:
            return False
    def isEmpty(self):
        if self.count ==0:
            return True
        else:
            return False
    
    def enqueue(self , val):
        if self.isFull():
            raise Exception("Queue is full || Queue is in overflow condition")
        else:
            if self.front == -1:
                self.front =0
            self.rear = (self.rear +1) % len(self.queue)
            self.queue[self.rear] =val
            self.count += 1
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty || Queue is in underflow condition")
        else:
            removed_Element = self.queue[self.front]
            self.front = ( self.front +1) % len(self.queue)
            self.count -= 1
            print(f"Element removed from the queue: {removed_Element}")

    def printQueue(self):
        if self.isEmpty():
            raise Exception("Queue is empty || Queue is in underflow condition")
        else:
            print("Queue elements:")
            for i in range(self.count):
                index = (self.front + i) % len(self.queue)
                print(self.queue[index],"--")


newQueue = circularQueue()
newQueue.enqueue(10)
newQueue.enqueue(20)
newQueue.enqueue(30)
newQueue.dequeue()
newQueue.enqueue(40)
newQueue.printQueue()