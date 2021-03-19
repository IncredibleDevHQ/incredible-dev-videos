a = [1 2 3 4]

a = [1 3 5; 2 4 6; 7 8 10]
  
z = zeros(5,1)    %you can also use zeros,ones or rand keywords to form matrices
  
a + 10            %can process all the elements using arithmetic operations or functions
a'
  
format long
p = a*inv(a)
