-- Conditional statements with IfElse
main = do   
   let x = 23 
   if x `rem` 2 == 0  --`rem` returns the remainder
      then putStrLn "Number is Even" 
   else putStrLn "Number is Odd"
