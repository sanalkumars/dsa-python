

class Node :
    def __init__(self , value):
        self.val = value
        self.left = None
        self.right = None

class Tree :

    def __init__(self):
        self.root = None
    
    def insertNode(self ,data):
        # creating the new node 
        newNode =  Node(data) 
        if self.root is None:
            self.root = newNode
            return self
        
        current = self.root
        while True :
            if data == current.val:  return self
            if data < current.val:
                if current.left is None:
                    current.left = newNode
                    return self
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    return self
                else:
                    current = current.right


        