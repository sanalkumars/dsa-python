

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

    def preOrderTraversal(self):
        self._preorderHelper(self.root)
        print()
        
    def _preorderHelper(self, node):
        if node is None:
            return
        print(node.val,end=" ") #visited the node
        self._preorderHelper( node.left) #visit the left side after root
        self._preorderHelper(node.right) # visit the right side after root

    def inorderTraversal(self):
        self._inorderHelper(self.root)
    
    def _inorderHelper(self , node):
        if node is None:
            return
        self._inorderHelper(node.left)
        print(node.val,end=" ")
        self._inorderHelper(node.right)

    # level by search or BFS
    # for this we need a doubly ended queue
    from collections import deque
    def breathFirstSearch(self):
        if not self.root:
            return
        queue = self.deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.val,end=" ")
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)


        

mytree = Tree()
mytree.insertNode(10)
mytree.insertNode(1)
mytree.insertNode(5)
mytree.insertNode(11)
mytree.insertNode(112)

# mytree.preOrderTraversal()

# mytree.inorderTraversal()


mytree.breathFirstSearch()


        