# Detecting Types

Create a function called `detector` that takes one parameter which can be anything (string, number, etc...).  Because the object given to your function can be anything, you want to know exactyly what type the object is.  Have your function both print a string which is the type of the object and also return a string which is the type of the object.  Test your function by sending it a list, a dictionary, and a string.  Hint: There is a built in python function which can tell you what type an object is.

# String lengths

Write a function called `lengths` that accepts a single parameter as an argument, which will be an array (list) of strings. The function should return an array of numbers. Each number in the array should be the length of the corresponding string. To get you started, you'll need to loop through each string in the array and get the length of each one. Those lengths should be stored in a different array that you will return.  To test your function, send it this array: ["word", "sentence", "paragraph"], which should return this array: [4, 8, 9].

# Getting Loony

Write a function called toonify that takes two parameters, accent and sentence.
If accent is the string "daffy", return a modified version of sentence with all "s" replaced with "th".
If the accent is "elmer", replace all "r" with "w".
If the accent is not recognized, just return the sentence as-is.

the result of this function is below:
```
toonify("daffy", "so you smell like sausage")
#=> "tho you thmell like thauthage"
```