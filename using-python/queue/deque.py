# this is for implementing a queue using deque in python

class Dequeue :
    def __init__(self):
        self.data =[]
        self.head =0
        self.tail =0

    def isEmpty(self):
        return self.head == self.tail and self.data[self.head] == None
    
    def insertAtTail(self , val):
        self.data.append(val)
        self.tail += 1

    def deleteAtTail(self):
        if self.isEmpty():
            return "queue is empty"
        self.data.pop()
    def insertAtHead(self, val):
        self.data.insert(0,val)
        self.tail += 1
    def deleteAtHead(self):
        if self.isEmpty():
            return "queue is empty"
        self.data.pop(0)


# testing the code
q = Dequeue()   
q.insertAtTail(1)
q.insertAtTail(2)
q.insertAtTail(3)
print(q.data) # [1, 2, 3]
q.deleteAtTail()
print(q.data) # [1, 2]
q.insertAtHead(0)
print(q.data) # [0, 1, 2]
q.deleteAtHead()
print(q.data) # [1, 2]