from collections import deque
def isvalid(i,j,r,c):
    if(i>=0 and i<r and j>=0 and j<c):
        return True
    else:
        return False
def isdelim(t):
    if(t[0]==-1 and t[1]==-1):
        return True
    else:
        return False
def checkall(a,r,c):
    for x in a:
        print(x)
    for i in range(r):
        for j in range(c):
            if(a[i][j]==1):
                return False
    return True
class Solution:
    def orangesRotting(self, a):
        r=len(a)
        c=len(a[0])
        Q=deque()
        t=[-1,-1]
        ans=0
        for i in range(r):
            for j in range(c):
                if(a[i][j]==2):
                    Q.append([i,j])
        Q.append(t)
		while(len(Q)!=0):
			flag=False
			while(not isdelim(Q[0])):
				t=Q[0]
				if(isvalid(t[0],t[1]-1,r,c) and a[t[0]][t[1]-1]==1):
					if(not flag):
						ans+=1
						flag=True
					a[t[0]][t[1]-1]=2
					Q.append([t[0],t[1]-1])
		       # right Adjacent
		        if(isvalid(t[0],t[1]+1,r,c) and a[t[0]][t[1]+1]==1):
		            if(not flag):
		                ans+=1
		                flag=True
		            a[t[0]][t[1]+1]=2
		            Q.append([t[0],t[1]+1])
		      # bottom Adjacent
		        if(isvalid(t[0]+1,t[1],r,c) and a[t[0]+1][t[1]]==1):
		            if(not flag):
		                ans+=1
		                flag=True
		            a[t[0]+1][t[1]]=2
		            Q.append([t[0]+1,t[1]])
		      # Top Adjacent
		        if(isvalid(t[0]-1,t[1],r,c) and a[t[0]-1][t[1]]==1):
		            if(not flag):
		                ans+=1
		                flag=True
		            a[t[0]-1][t[1]]=2
		            t[0]-=1
		            Q.append([t[0]-1,t[1]])
		            t[0]+=1
		        Q.popleft()
		        #print(Q)
		 
		    Q.popleft()  
		    if(len(Q)!=0):
		        t=[-1,-1]
		        Q.append(t)
		if(checkall(a,r,c)):
		    return ans
		    
		else:
		    return -1
	

r,c=list(map(int,input().split()))
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))
print(Solution().orangesRotting(a))




            





    


