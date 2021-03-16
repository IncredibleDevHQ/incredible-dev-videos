void main() {
  //Set<DataType> name;
  //var name = <DataType>{}
  Set<int> nums;
  
  var set1 = {'a' , 'e', 'i'};
  var set2 = {'o'};
  
  set2.add('u');
  set1.addAll(set2);
  
  print(set1);
  //{a, e, i, o, u}
}
