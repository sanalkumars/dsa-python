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

    def printLinkedList(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print("<=>",current.data,"<=>")
                current=current.next

# creating a doubly lisked list using the class
list = DoublyLinkedList()

# calling insert funcation for the end insert
list.InsertNewNodeAtEnd(10)
list.InsertNewNodeAtEnd(20)
list.InsertNewNodeAtEnd(30)
list.InsertNewNodeAtEnd(40)

list.printLinkedList()
