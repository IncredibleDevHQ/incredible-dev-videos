/* Sometimes you cant start with nothing.
 * Lets give em something :) */

class Point {
  int x = 0;
  int y = 0;

  Point(this.x, this.y) {
    print("In constructor");
  }
  //Point(this.x , this.y);

  Point.named(this.x, this.y) {
    print("In named constructor");
  }
}

void main() {
  var p1 = Point(10, 5);
  // In constructor
  print(p1.x + p1.y); //15
  var p2 = Point.named(10, 20);
  // In named constructor
  print(p2.x + p2.y); //30
}