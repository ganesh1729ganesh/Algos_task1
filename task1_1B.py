

print("The length of the string is always a power of 2 to find degree of symmetry")
lenStr = int(input("Enter the length of the string: " ))
symStr = input("Enter the string: ")

def degOfSymm(symStr):
    n = lenStr
#checking the length of the string is odd or even to find further symmetry    
    if n%2==0: 
        mid = n//2    
    else: 
        mid = n//2 +1
    p1 = 0
    p2 = mid
    count = 0
#looping the condition that euals the symmetrical halves         
    while symStr[p1:p2] == symStr [p2: n]:
#Re-assigning the variables to new vlues to continue the loop and can find symmetrical strings present inside   
        p1 = 0
        n = p2
        p2 = p2 //2 
       
        count +=1#increasing count for every time loop runs which is for every symmetrical strings
            
    return count

result = degOfSymm(symStr)#calling the function defined
print("The degree of symmetry of given string is: ",result )
            
"""
since there is a single loop + few conditionals
Time complexity is O(n) + k = O(n)
Here
    space complexity is based on length of the string + int variables
    
    ==> n + 24*c
        O(n) is the time complexity """
