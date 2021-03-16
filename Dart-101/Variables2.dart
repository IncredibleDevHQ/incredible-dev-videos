void main() {
  int? x; // holds null
  
  late String name1;
  //print(name1) throws Error
  name1 = "Hello";
  late String name2 = "World";
  
  final year = 2021;
  //final int year = 2021;
  const pi = 3.14;
  
  print("$x $name1 $name2 $year $pi");
  //null Hello World 2021 3.14
}
