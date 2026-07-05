
class Node :
    def __init__(self , value):
        self.val = value
        self.left = None
        self.right = None

class BST :
    def __init__(self):
        self.root = None
    
    # insertion in a BST 

    def insert( self , value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._inertHelper(self.root , value)

    

    def _inertHelper(self ,current, value ):
        if value < current.val:
            if current.left is None:
                current.left = Node(value)
            else:
                self._inertHelper(current.left , value)
        elif value > current.val:
            if current.right is None:
                current.right = Node(value)
            else:
                self._inertHelper(current.right, value)

    def searchNode(self , value):
        return self._searchHelper(self.root , value)


    def _searchHelper( self , node , value):
        if node is None :
            return False
        if node.val == value:
            return True
        elif value < node.val:
            return self._searchHelper(node.left, value)
        else :
            return self._searchHelper(node.right, value)

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
    
    # node deletion 
    def deleteNode(self, val):
        if self.searchNode(val):  # Check if node exists
            self.root = self.deleteNodeHelper(self.root, val)
            return True
        return False
        
        
    def deleteNodeHelper( self, node, val):
        if not node :
            return  None
        if val < node.val :
            return self.deleteNodeHelper( node.left , val)
        elif val > node.val:
            return self.deleteNodeHelper(node.right , val)
        else: #found the node
            #case one (leaf node)
            if not node.left and not node.right:
                return None
            #case2 one child node
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # two child node present 
            successor = self.findMin(node.right)
            node.val = successor.val
            node.right = self.deleteNodeHelper(node.right , successor.val)
        return node
    
    # search/find node
    def find_node( self , key):
        current = self.root
        while current is not None  and current.val != key:
            current = current.left if key < current.val else current.right
        return current
            
    # find the successor
    def find_Successor(self , key):
        candidate = None
        curr = self.root

        while curr is not None:
            if key < curr.val:
                candidate = curr
                curr = curr.left
            elif key > curr.val:
                curr = curr.right
            else:
                # found the node/key
                if curr.right is not None :
                    return self.findMin(curr.right)
                break
        return candidate.val
     

    # find the predecessor 
    def find_Predecessor( self , key):
        candidate = None
        curr = self.root

        while curr is not None:
            if key < curr.val:
                curr = curr.left
            elif key > curr.val:
                candidate = curr
                curr = curr.right
            else:
                # we found the key in the tree , here two case if there is a left subtree with max-value then return that , else returnt 
                # current candidate 
                if curr.left is not None:
                    return self.findMax(curr.left)
                break
        return candidate.val

           

    def findMin( self ,node ):
        current = node
        while current.left:
            current = current.left
        return current.val
    
    def findMax(self , node):
        current = node
        while current.right:
            current = current.right
        return current.val


    # height of the tree
    def height_Of_Node(self, key):
        # find the node first
        node = self.find_node(key)
        return self.getHeight(node)

        
        # compute the height 
    
    def getHeight( self , node):
        if node is None:
            return -1
        return 1 + max( self.getHeight(node.left) , self.getHeight(node.right))
        
        

        
bst = BST()
    
    # Insert values
values = [20, 30, 40, 45, 50, 60, 70, 80]
for val in values:
    bst.insert(val)



# bst.breathFirstSearch()
# print(" Search result is  :", bst.searchNode(20))  
# print(" Deleted result is  :", bst.deleteNode(20))  

# print("the successor of the value 45",bst.find_Successor(45))
# print("the predecessor of the value 45",bst.find_Predecessor(45))


# print("node found ",bst.find_node(30))
print("Height of the node is :",bst.height_Of_Node(40))