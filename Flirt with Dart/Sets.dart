void main() {
  //Set<DataType> name;
  //var name = <DataType>{}
  Set<int> nums;
  
  var set1 = {'a' , 'e', 'i'};
  var set2 = {'o'};
  
  set2.add('u');
  set2.add('a'); //{o, u, a}
  
  set1.addAll(set2);
  // repeated 'a' is omitted
  print(set1);
  //{a, e, i, o, u}
}
