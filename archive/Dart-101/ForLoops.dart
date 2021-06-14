/* Easy way to do the same thing 
 * again and again and again and
 * ... you get the point */

void main() {
  for(var i = 0; i<10; i++){
    print(i);
  }
  //0123456789
  
  var list = ['How','are','you?'];
  for(var word in list) {
    print(word);
  }
  //How are You?
  
  list.forEach((word) => print(word));
}