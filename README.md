# Practice-programs
Final Test 1
Write a function which will take an integer as input and print each digit in a separate line. You are not allowed to use str or any other method will convert the integer into string.

Final Test 2
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.Assignment

Final Test 3
You are given a positive integer. You can only use one for loop and one print statement. Print a numerical triangle of height like the one below:Assignment

Final Test 4
You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace these consecutive occurrences of the character 'c' with (4, c) in the string.Assignment

Final Test 5
Remove symbols from the string

Final Test 6
You get an array of numbers, and return the sum of all of the positive ones. Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the if statement.Assignment

Final Test 7
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ). You can not use the if statement.Assignment

Final Test 8
Calculate total score

Final Test 9
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.Assignment

Final Test 10
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.Assignment

Final Test 11
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.Assignment

Final Test 12
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Final Test 13
Your task is to create a program which will play Rock Paper Scissors with the user. Take input from the user for his/her selection like scissors/rock/paper. Program should select randomly rock/paper/scissors. Output should be indicating who won the user or computer.

Final Test 14
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

Final Test 15
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false.

Final Test 16
Complete the solution so that the function will break up camel casing, using a space between words.

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""   =>  ""
Final Test 17
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p. we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.Assignment

Final Test 18
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.Assignment

Final Test 19
Write a function that accepts a fight string consisting of only small letters and return who wins the fight. When the left side wins, the Left side wins!, when the right side wins, the Right side wins!, in other cases, Let's fight again!.
Left side letters

 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (pretty word)

Right side letters:

 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (pretty word)

The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly letters with the same power.

alphabet_war("z") #=>  "z"  => "Right side wins!"

Explanation:
Letter z belongs to the right side letters and the left side has no letter so the right side wins.


alphabet_war("tz")        #=>  "ts" => "Left side wins!"

Explanation:
Letter t is a pretty letter belonging to the left side. Pretty letters convert hostile letters to friendly letters with the same power. Z is a hostile letter with power 1. T will convert it to s a friendly letter with the same power.

Final Test 20
Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in the following way:
All the elements in the first and last row and column are 1.
All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
