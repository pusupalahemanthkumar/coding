def getUglyNum(n):
    ugly=[0]*n 
    ugly[0]=1

    i2=i3=i5=0

    next_m_2=2
    next_m_3=3
    next_m_5=5

    for i in range(1,n):
        ugly[i]=min(next_m_2,next_m_3,next_m_5)

        if(ugly[i]==next_m_2):
            i2+=1
            next_m_2=ugly[i2]*2
        if(ugly[i]==next_m_3):
            i3+=1
            next_m_3=ugly[i3]*3
        if(ugly[i]==next_m_5):
            i5+=1
            next_m_5=ugly[i5]*5
    return ugly[-1]

n=int(input())
print(getUglyNum(n))
