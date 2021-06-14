extension JS on List {
  pop(){
    return this.removeLast();
  }    
  
  push(value) {
    this.add(value);
  }
  
  shift() {
    return this.removeAt(0);
  }
  
  unshift(value){
    this.insert(0, value);
  }
}

void main() {
  var list = [11,21,32,45,59];
  
  list.pop();
  print(list); //[11, 21, 32, 45]
  
  list.push(59);
  print(list); //[11, 21, 32, 45, 59]
  
  list.shift();
  print(list); //[21, 32, 45, 59]
  
  list.unshift(11);
  print(list); //[11, 21, 32, 45, 59]
}
