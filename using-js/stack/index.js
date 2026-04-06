// this file contains the stack implementation using an array

class Stack {
  constructor() {
    this.stack = [];
  }

  push(value){
    this.stack.push(value);
  }

  pop(value){
    this.stack.pop(value);
  }

  peek(){
    return this.stack[this.stack.length-1];
  }

  print(){
    // console.log(this.stack,"->");
    for(let i = this.stack.length-1; i >= 0; i--){
      console.log(this.stack[i], "->");
    }
  }
}

// example usage
const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.print(); // [1, 2, 3]
console.log(stack.peek());
stack.pop();
stack.print(); // [1, 2]