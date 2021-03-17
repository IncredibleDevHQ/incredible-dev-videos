/* Let's build some buildings. Where 
 * did we keep those blueprints again? */

class Point {
  double x = 10.0;
  double y = 5.0;

  void update(double x, double y){
    this.x = x;
    this.y = y;
  }
}

void main() {
  var p1 = Point();
  print(p1.x + p1.y); //15
  p1.update(12.0, 8.0);
  print(p1.x + p1.y); //20
  
  var p2 = Point();
  print(p1 == p2); //false
}
