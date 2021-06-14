/* You are special.Some things only you can do.
   What about mosquitoes though? */

abstract class Insect{
  void crawl() =>  print("crawl");
}

mixin Flutter on Insect{
  void flutter() => print("flutter");
}

class Mosquito 
  extends Insect with Flutter {
  void doMosquitoThing(){
    crawl();
    flutter();
    print("suck blood");
  }
}

void main() {
  var m = Mosquito();
  m.doMosquitoThing();
}