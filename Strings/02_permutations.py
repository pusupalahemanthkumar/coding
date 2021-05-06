import itertools
class Solution:
    def find_permutation(self, S):
        # Code here
        iterator=itertools.permutations(list(S))
        res=[]
        for i in iterator:
            res.append("".join(i))
        return sorted(res)
s=input()
res=Solution().find_permutation(s)
for i in res:
    print(i,end=" ")