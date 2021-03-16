#Lets look at If Else and Switch Case

void main() {
  int a = 2;
  
  if(a == 1) {
    print("1");
  } 
  else if(a == 2) {
    print("2");
  } 
  else {
    print("not 1 or 2");
  }
  
  switch(a) {
      case 1 : print("1");break;
      case 2 : print("2");break;
      default : print("not 1 or 2");break;
  }
}
