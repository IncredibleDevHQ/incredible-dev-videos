/* Sometimes you cant start with nothing.
 * Lets give em something :) */

class Point {
  int? x;
  int? y;

  Point() {
    x = 5;y = 10;
    print("$x $y");
  }

  Point.named(this.x, this.y) {
    print("Named : $x $y");
  }
}

void main() {
  var p1 = Point();
  // 5 10
  var p2 = Point.named(10, 20);
  // Named : 10 20
}
