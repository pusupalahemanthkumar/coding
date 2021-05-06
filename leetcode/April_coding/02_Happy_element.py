# link - https://www.youtube.com/watch?v=Egw03gI-Tf0&list=PLEJXowNB4kPwCPVjDv6KsAsThtDOCQUok&index=2&ab_channel=TECHDOSE

def isHappy(num):
    f={num}
    while(1):
        c_num=sum([int(i)*int(i) for i in str(num)])
        print(c_num,f)
        if(c_num==1):
            return True
        if(c_num in f):
            return False
        else:
            f.add(c_num)
        num=c_num
        print(f)

num=int(input())
print(isHappy(num))

