class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
    
    # insert at end
    def insertEnd(self,value):
        # we create a new node using the Node class, also asign it to a new variable
        temp = Node(value)
        if(self.head !=None):
            current = self.head
            while(current.next !=None):
                current=current.next
            current.next=temp
        else:
            self.head = temp
    
   

    def printLinkedList(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,"->")
                current=current.next
            # print(current.data)

list = SinglyLinkedList()

list.insertEnd(30)
list.insertEnd(40)
list.insertEnd(50)

list.printLinkedList()
        