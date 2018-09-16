"""
You are given two strings. You have to check if the strings are permutations of each other and output "YES" or "NO" accordingly without quotes.

Input: 
2 lines of input each containing a string. (a to z and 0 to 9) 
Output: 
A single line containing YES or NO.

Constraints:
String would not contain any spaces. size of string < 100 
NOTE : This is a golf question. Shorter code will get highest points.
"""

from collections import Counter
print("YES" if Counter(input()) == Counter(input()) else "NO")
