/* Want to make a todo with me? */

void main() {
  var list = ["Wakeup","Learn","Sleep",];
  // var list = const ["Wakeup","Learn","Sleep"];
  print("${list[0]},${list[1]}");
  // Wakeup, Learn
  print(list.length); 
  // 3
  
  /* Dynamic list and spread operator */
  var list2 = [0, ...list];
  print(list2);
  // [0, Wakeup, Learn, Sleep]
}
