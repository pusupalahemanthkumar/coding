num=int(input())

mem=[-1]*(num+1)
mem[0]=0

for i in range(1,num+1):
    mem[i]=mem[i//2]+i%2
print(mem)