a = [1 2 3 4]
    1     2     3     4

a = [1 3 5; 2 4 6; 7 8 10]
    1     3     5
    2     4     6
    7     8    10
  
z = zeros(5,1)    %you can also use zeros,ones or rand keywords to form matrices
     0
     0
     0
     0
     0
  
a + 10            %can process all the elements using arithmetic operations or functions
    11    13    15
    12    14    16
    17    18    20
  
format long
p = a*inv(a)
  0.999999999999996         0                0
           0       1.000000000000000         0
           0      -0.000000000000014   1.000000000000000

