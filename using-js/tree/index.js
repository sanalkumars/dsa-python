

class Node {
    constructor( value ){
        this.value = value;
        this.right = null;
        this.left = null;
    }
}

class Tree {
    constructor(){
        this.root = null;
        this. res = [];
    }

    emptyRes(){
        this.res =[];
    }

    // inserting a new value 

    insertNewNode(val){
        let newNode = new Node(val);
        // case 1 root is empty
        if( !this.root) {this.root = newNode ; return this;}

        let current = this.root;
        while( true ){
            if( val === current.value) return this;
            if( val < current.value){
                // CHECKS IF THE LEFT IS EMPTY , THEN ASSIGN THE VALUE TO LEFT
                if( !current.left) { current.left = newNode ;  return this;}
                current = current.left
            }else{
                if( !current.right) { current.right = newNode ; return this;}
                current = current.right
            }

        }
    }

    // traversal 
    // 1. InOrder 2.PreOrder 3.POST order
    
    inOrder( node = this.root ){
        if( !node) { return this.res}
        console.log("returns without assigning")
        this.inOrder( node.left );
        this.res.push( node.value);
        this.inOrder( node.right);
    }

    preOrder( node = this.root){
        if( !node ) { return this.res}

        this.res.push(node.value);
        this.preOrder(node.left);
        this.preOrder(node.right);
    }

    postOrder( node = this.root){
        if( !node) { return this.res}
        this.postOrder(node.left);
        this.postOrder(node.right);
        this.res.push(node.value)
    }
}

let newBST = new Tree();

newBST.insertNewNode(10);
newBST.insertNewNode(9);
newBST.insertNewNode(11);

newBST.inOrder()
console.log(newBST.res , " => final node list")
newBST.emptyRes();
newBST.preOrder()
console.log(newBST.res , " PRE order traversal result")
newBST.emptyRes();

newBST.postOrder()
console.log("post order traversal result is ", newBST.res)


