// Node class - each element in linked list
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// LinkedList class
class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }
    
    // Add node at end (append)
    append(value) {
        const newNode = new Node(value);
        
        if (!this.head) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
        this.size++;
    }
    
    // Add node at beginning (prepend)
    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        this.size++;
    }
    
    // TRAVERSE (print all values)
    traverse() {
        let current = this.head;
        const values = [];
        
        while (current) {
            values.push(current.value);
            current = current.next;
        }
        console.log("Linked List:", values.join(" → "));
        return values;
    }
    
    // Alternative traversal with indices
    printWithIndex() {
        let current = this.head;
        let index = 0;
        console.log("Index | Value");
        while (current) {
            console.log(`${index}    | ${current.value}`);
            current = current.next;
            index++;
        }
    }
}

// USAGE EXAMPLE
const list = new LinkedList();

// Create linked list
list.append(1);
list.append(2);
list.append(5);
list.append(4);
list.append(8);

// Insert at beginning
list.prepend(0);

// TRAVERSE
console.log("=== Basic Traversal ===");
list.traverse();  // Output: 0 → 1 → 2 → 5 → 4 → 8

console.log("\n=== With Indices ===");
list.printWithIndex();

console.log(`\nSize: ${list.size}`);
