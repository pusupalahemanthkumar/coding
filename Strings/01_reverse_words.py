class Solution:
    # User function Template for python3
    
    def reverseWords(self,S):
        # code here 
        a=S.split(".")
        return ".".join(a[::-1])

s=input()
print(Solution().reverseWords(s))