baseInputs = list(map(int, input("Enter the details such as total  no. of days of contest, initial rating , rating increment parameter , rating decrement parameter in order : ").split()))

#map fn maps integer fn to the input str values and split function splits them, since no delimeter is passed it takes a space as a delimeter

contest = list(map(int , input(" Enter 1 if contest took place on ith day or else enter 0 : ").split()))
#storing them in a list for further access

scn = list(map(int , input ( " Enter 1 if Adit ate SCN on the ith day or else enter 0:  ").split()))
#storing them in a list for further access

n = baseInputs[0]#no. of days that the contest takes place
r = baseInputs[1]#initial rating
x = baseInputs[2]#rating increment parameter
y = baseInputs[3]#rating decrement parameter 

i = 0
j = 0

#iterating over number of days
for day in range(1,n+1):
    for i in contest:#iterating over the days that adit participate in contest
        for j in scn :#iterating over the days that adit ate scn
            if i==1 and j == 1: #if both are done in same day he performs well and automatically his rating increase
                r+=x
               
            else:
                r-= y #or else his rating decreases
if r > baseInputs[1]:
    print("promoted")
elif r < baseInputs[1]:#comparison with initial values
    print("demoted")
else:
    print("no change")


"""
    TIME COMPLEXITY:
                    since there are 3 loops time complexity is O(n^3)
    SPACE COMPLEXITY:
                    since only integers are present i.e.,24*k
                    O(1),constant """
