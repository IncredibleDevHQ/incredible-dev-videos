new()   Creates a new empty String
let empty_string = String::new();

to_string()   Converts the given value to a String.

len()   Returns the length of this String, in bytes.
content_string.len()

replace()  
let name1 = "Hello Incredibles', Hello!".to_string();
let name2 = name1.replace("Hello","Howdy");

push()    appends the given char to the end of this String
let company = "Incredible".to_string();
company.push('s');
