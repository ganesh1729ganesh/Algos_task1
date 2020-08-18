
lenBin= int(input("Enter the length of your binary string: "))#24 bytes
#length of the input binary string
binStr = input("Enter the binary string that you want to decompose: ")
#The binary string the user wants to decompose
"""
The int() function converts the binary string into base 2 number
that  is a binary number , it takes two arguments first is the required argument and the second is to which base
since we want a binary string base 2 is provided
"""   
   
decVal = int(binStr,2)
decVal = decVal * 2 #24 Bytes
"""
let S be the main string we want to decompose, so doubling the decimal value
of the binary string and finding possible order pairs and finally converting
them to binary strings is the core idea.
 S = (s1 + s2)/2
 2S = S1 + S2
"""
i = 0 #24 bytes
j = 0 #24 bytes

for i in range (0, decVal+1):
#iterating over the range from 0 to decimal value of the binary string
    for j in range(0,decVal - i +1 ):
#iterating over the complementary values in making sum equals to decimal value of the binary string
        if i+j == decVal :
            #print(i,j)
            i = bin(i)[2: ]
            j= bin(j)[2: ]
            len_i = len(str(i))
            len_j = len(str(j))
            if lenBin == len_i and lenBin == len_j :#comparing the lengths to make sure that all are of same lengths as of original string
                if i < j:#to make sure that in the order pairs first value is less than 2nd value
                    print(i + " " + j)
else:
    print("-1 - The program is completed")



"""
Time complexicity:
let the complexity of all the statements is c1
since there are two for loops for each loop the statement is executed n times in inner loop and each
inner loop is iterated another n times
the total complexity is O(n^2) or BigO(n^2)
Space complexicity: The space complexity is a no. of int variables * 24 bytes
that is c* 24 = O(1) , constant"""
