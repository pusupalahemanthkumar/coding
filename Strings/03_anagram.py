
class Solution:  
    def isAnagram(self,a,b):
        #code here
        if(len(a)!=len(b)):
            return False
        f1=dict.fromkeys(set(a),0)
        f2=dict.fromkeys(set(b),0)
        for i in a:
            f1[i]+=1
        for j in b:
            f2[j]+=1
        for i in a:
            if(f1.get(i)!=f2.get(i)):
                return False
        return True

print(Solution().isAnagram(input(),input()))