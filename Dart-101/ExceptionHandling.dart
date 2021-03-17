/* Always good to be prepared for a disaster */

void main() {
  var x = 10, y = 0;
  
  try{
    if(y == 0)
      throw Exception("Division by 0");
    else 
      print(x/y);
  } 
  on IntegerDivisionByZeroException catch(e){
    print(e);
  } 
  catch(e, s){
    print(e); //Division by 0
    print(s); //stacktrace
  } 
  finally {
    print("Oof caught that one!");
  }
}