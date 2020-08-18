"""

Adit wants to write a program that gives the exact order of the sequence considering
the answers he receives from Advay. Formally, the program should give the output for whatever
answers Advay gives for Adit’s queries(Advay’s answers are always a product of 2 numbers (taken from
the above sequence)


"""
baseArray = [ 10,8,7,16,9,43]
print("Hey advay ! Let's begin the game, tell me about numbers at indices 0 and 1 ")
ans1 = int(input("The product of numbers present in the index positions 0 and 1 is: "))

print(" Tell me about numbers at indices 1 and 2 ")
ans2 = int(input("The product of numbers present in the index positions 1 and 2 is: "))

print("Tell me about  numbers at indices 2 and 3 ")
ans3 = int(input("The product of numbers present in the index positions 2 and 3 is: "))

print("Tell me about  numbers at indices 3 and 5 ")
ans4 = int(input("The product of numbers present in the index positions 3 and 5 is: "))

def f1():
    for i in baseArray:
        if ans1 % i == 0 and i <44 and i>6 and i in baseArray:
            if ans1//i < 44 and ans1//i >6 and ans1//i in baseArray :
                return [i,ans1//i]
#iterating in the baseArray and checking the possible values that are possible and providing limits
x = f1()


def f2():
    for j in baseArray:
        if ans2 % j == 0 and j < 44 and j>6 and j in baseArray:
            if ans2//j < 44 and ans2//j >6 and ans2//j in baseArray :
                return [j,ans2//j]
#iterating in the baseArray and checking the possible values that are possible and providing limits
y = f2()


def f3():
    for k in baseArray:
        if ans3 % k == 0 and k < 44 and k>6 and k in baseArray:
            if ans3//k <44 and ans3//k >6 and ans3//k in baseArray:
                return [k,ans3//k]
#iterating in the baseArray and checking the possible values that are possible and providing limits
z = f3()


def f4():
    for m  in baseArray:
        if ans4 % m == 0 and m < 44 and m >6 and m in baseArray:
            if ans4//m < 44  and ans4//m > 6 and ans4//m in baseArray:
                return [m,ans4//m]
#iterating in the baseArray and checking the possible values that are possible and providing limits
w = f4()

p1 = set(x).intersection(set(y))#checking common value in x and y and inserting the value at index 1
p2 = set(y).intersection(set(z))#checking common value in y and z and inserting the value at index 2
p3 = set(z).intersection(set(w))#checking common value in z and w and inserting the value at index 3

lis = []
e = ans1//list(p1)[0] #in ans1 , since it's a product of numbers at indices 0 and 1 , we now know number at index 1,so divding it by product yields number at index 0
f = ans4//list(p3)[0]#in ans4 , since it's a product of numbers at indices 3 and 5 , we now know number at index 3,so divding it by product yields number at index 5

list_main = [e,list(p1)[0],list(p2)[0],list(p3)[0],f]

g = set(baseArray).difference(set(list_main))# now we got 4 elements, the 5th element is the difference of this list and baseArray yields missing element

sequence = [e,list(p1)[0],list(p2)[0],list(p3)[0],list(g)[0],f]

print("Hey! Advay the exact sequence is: ", sequence)



"""
tIME COMPLEXITY:
                since we have four for loops
                4*n + k
                therefore
                        time complexity is O(n)


SPACE COMPLEXITY:
                here only integers so num. of integers * 24 bytes
                there time complexity is:
                                O(1),constant
"""









