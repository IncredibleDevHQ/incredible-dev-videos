// Conditional Expressions and Cascading

void main() {
  // condition ? exp1 : exp2
  var x = 1;
  String result = (x>0) ? "Positive" : "Negative";
  print(result); //Positive
  
  //cascading
  var paint = Paint()
    ..color = Colors.black
    ..strokeCap = StrokeCap.round
    ..strokeWidth = 5.0;
}
