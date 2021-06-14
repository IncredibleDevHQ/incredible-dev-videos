/* When you can be something more */

void main() {
  // String -> int
  var one = int.parse('1');
  print(one == 1); //true

  // String -> double
  var onePointOne = double.parse('1.1');
  print(onePointOne == 1.1); //true

  // int -> String
  String oneAsString = 1.toString();
  print(oneAsString == '1'); //true

  // double -> String
  String piAsString = 3.14159.toStringAsFixed(2);
  print(piAsString == '3.14'); //true
}
