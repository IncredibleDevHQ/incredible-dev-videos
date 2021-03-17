/* Why create new stuff when the 
 * one we have works just fine? */

class Dad {
  int money = 100000;
  void say() {
    print("Hey son take this!");
  }
}

class Son extends Dad {
  @override
  void say() {
    super.say();
    print("Thanks dad for $money");
  }
}

void main() {
  var s = Son();
  s.say();
  // Hey Son!
  // Thanks dad for 100000
}
