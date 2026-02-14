Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. 
It states that every even number greater than 2 is the sum of two prime numbers.

For Example:

12 = 5 + 7

26 = 3 + 23 or 7 + 19 or 13 + 13

Write a function Goldbach(n) where n is a positive even number (n > 2) 
that returns a list of tuples.

In each tuple (a, b):
- a <= b
- a and b should be prime numbers
- a + b should be equal to n

Sample Input 1
12

Output
[(5,7)]

Sample Input 2
26

Output
[(3,23),(7,19),(13,13)]