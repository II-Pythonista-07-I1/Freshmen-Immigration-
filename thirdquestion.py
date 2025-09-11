'''Problem: Positive, Negative, or Zero

Write a Python program that:

Asks the user to enter 20 numbers.

Checks if each number is positive, negative, or zero.

Prints the result.'''

n1,n2,n3,n4,n5,n6,n6,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20=map(int,input().split()); [print(f'{n} is posotive') if n>0 else print(f'{n} is negative')if n<0 else print('Zero!!!') for n in (n1,n2,n3,n4,n5,n6,n6,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20)] 
