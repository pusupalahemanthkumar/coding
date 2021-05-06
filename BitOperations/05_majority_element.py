n=int(input())
a=list(map(int,input().split()))

def findMajority(arr, n):
    # Number of bits in the integer
    Len = 32

    # Variable to calculate majority element
    number = 0
  
    # Loop to iterate through 
    # all the bits of number
    for i in range(Len):
        count = 0
          
        # Loop to iterate through all elements 
        # in array to count the total set bit
        # at position i from right
        for j in range(n):
            if (arr[j] & (1 << i)):
                count += 1
                  
        # If the total set bits exceeds n/2,
        # this bit should be present in 
        # majority Element.
        if (count > (n // 2)):
            number += (1 << i)
  
    count = 0
  
    # iterate through array get
    # the count of candidate majority element
    for i in range(n):
        if (arr[i] == number):
            count += 1
  
    # Verify if the count exceeds n/2
    if (count > (n // 2)):
        print(number)
    else:
        print("Majority Element Not Present")

print(findMajority(a,n))
