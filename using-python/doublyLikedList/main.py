class Node:
    def __init__(self,value, next = None , prev=None):
        self.data = value
        self.prev = prev 
        self.next = next

class DoublyLinkedList:
    def __init__(self , head=None):
        self.head = head   

    def InsertNewNodeAtEnd( self , value ):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head

        while( temp.next ):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def InsertAtBegining(self , value):
        newnode = Node(value)

        if( self.head is None):
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev
        self.head = newnode

    def InsertAtAnywhere( self , value , pos):
        newnode = Node(value)
        # condition 0 is the list is empty
        if self.head is None:
            print("the list is empty so the value is insert at the begining")
            self.head = newnode
            return
        # condition 1 selected position is the first position 
        if pos == 1:
            newnode.next = self.head
            if self.head  is not None:
                self.head.prev = newnode
            self.head = newnode
            return
        
        count = 1
        temp = self.head
        prev = None
        while( temp is not None and count < pos ):
            prev = temp
            temp = temp.next
            count +=1

        if temp is None and count < pos :
            print(f"position {pos} is out of bound ")
            return
        
        prev.next = newnode
        newnode.prev = prev
        newnode.next = temp
        if temp is not None:
            temp.prev = newnode
        


    def printLinkedList(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print(current.data,end="<=>")
                current=current.next

# creating a doubly lisked list using the class
list = DoublyLinkedList()

# calling insert funcation for the end insert
list.InsertNewNodeAtEnd(10)
list.InsertNewNodeAtEnd(20)
list.InsertNewNodeAtEnd(30)
list.InsertNewNodeAtEnd(40)

list.InsertAtBegining(9)

list.InsertAtAnywhere(8,3)


list.printLinkedList()
