/* What if... blueprints had blueprints
 * Woahh... Blueprint-ception :O */

abstract class Doer {
  // Define an abstract method.
  void doSomething();
}

class EffectiveDoer extends Doer {
  void doSomething() {
    print("Let's party!");
  }
}

void main() {
  var d = EffectiveDoer();
  d.doSomething();
}