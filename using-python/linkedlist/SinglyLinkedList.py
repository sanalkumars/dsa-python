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
    
    def insertStart(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head= newnode
            return
        temp = self.head
        self.head = newnode
        newnode.next = temp
    
    def inserAtAnywhere(self,value,pos):
        newnode = Node(value)
        if pos == 0 or self.head is None:
            newnode.next = self.head
            self.head= newnode
            return
        current = self.head
        count = 0
        while count < pos-1 and current.next is not None:
            current = current.next
            count +=1

        if count != pos - 1:
            print(f"Position {pos} is out of bounds")
            return
        newnode.next = current.next
        current.next= newnode

    def deleteNode(self , value ):
        if self.head is None:
            print("List is empty")
            return 
        prev = None
        temp = self.head

        if( value == self.head.data):
            self.head = self.head.next
            print(f"element { value } has been removed from the list")
            self.printLinkedList()
            return
        while(temp.next and temp.data != value):
            prev = temp
            temp = temp.next
        if( temp.data == value):
            prev .next = temp.next
            self.printLinkedList()
        else:
            print(f"Element { value } not found in the list")


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

list.insertEnd(20)
list.insertEnd(30)
list.insertEnd(40)
list.insertEnd(50)

# list.insertStart(20)

list.inserAtAnywhere(60,3)
# list.printLinkedList()

list.deleteNode(50)
        