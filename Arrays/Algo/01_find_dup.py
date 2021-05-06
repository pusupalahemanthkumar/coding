# link- https://www.youtube.com/watch?v=32Ll35mhWg0&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2

def findDuplicate(nums,n):
    slow=nums[0]
    fast=nums[0]
    while(1):
        slow=nums[slow]
        fast=nums[nums[fast]]
        if(slow==fast):
            break
   
    fast=nums[0]
    while(slow!=fast):
        slow=nums[slow]
        fast=nums[fast]
    return slow



n=int(input())
a=list(map(int,input().split()))
print(findDuplicate(a,n))