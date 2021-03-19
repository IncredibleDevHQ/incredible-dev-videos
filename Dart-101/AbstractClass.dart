/* What if... blueprints had blueprints
 * Woahh... Blueprint-ception :O */

abstract class Doer {
  // Define an abstract method.
  void doSomething();
}

class EffectiveDoer1 extends Doer {
  void doSomething() {
    print("Let's party!");
  }
}

class EffectiveDoer2 extends Doer {
  void doSomething() {
    print("Let's sleep");
  }
}

void main() {
  var d1 = EffectiveDoer1();
  var d2 = EffectiveDoer2();
  d1.doSomething();
  d2.doSomething();
}
