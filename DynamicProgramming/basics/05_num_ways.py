'''
link - https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).
'''

def bruteFore(n):
    if(n<0):
        return 0
    if(n==0):
        return 1
    return bruteFore(n-1)+bruteFore(n-3)+bruteFore(n-5)

def solve(n,lookup={}):
    if(n<0):
        return 0
    if(n==0):
        return 1
    for i in range(1,n+1):
        if(i not in lookup):
            lookup[n]=solve(n-1)+solve(n-3)+solve(n-5)
    return lookup[n]
n=int(input())
print(bruteFore(n))
print(solve(n))