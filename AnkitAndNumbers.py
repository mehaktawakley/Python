"""
Ankit has a set of numbers and has recently studied set theory. He has created a power set of this set and is writing a program to compute sum of all elements of all the subsets in power set. 
Power set of a set S is defined as set of all possible subsets of S.

Set S consist of all the number from 1 to N.

You need to calculate this sum for a given n.

Example:
Given N=3,
S={1,2,3}
P(S) = {{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
answer = (1)+(2)+(3)+(1+2)+(1+3)+(2+3)+(1+2+3)
= 24

Input
First line has T, the total number of test cases.
The next T lines contains a number N in each line.

Output
T lines giving answer as defined in the question for each N.

Constraints
1<=T<=42
1<=N<=42

SAMPLE INPUT 
1
3
SAMPLE OUTPUT 
24
"""

t = int(input())

while t>0:
    n = int(input())
    sumn=0
    for i in range(1,n+1):
        sumn += (2**(n-1))*i
    print(sumn)
    t-=1