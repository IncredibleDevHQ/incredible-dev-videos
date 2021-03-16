void main() {
  var list = [1,2,3,];
  // var list = const [1,2,3];
  print("${list[0]},${list[1]}");
  // 1,3
  print(list.length);
  // 3
  
  var list2 = [0, ...list];
  print(list2);
  // [0, 1, 2, 3]
}
