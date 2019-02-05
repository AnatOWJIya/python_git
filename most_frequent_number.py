a = [int (x) for x in input("Enter  number sequence:\n").split()]
b = []
#dict = {}
min = 0
big = 0
number = 0
length = 0
big = a.count(a[0])
for i in a:
    #big = a.count(i)
    if a.count(i) >= big and i not in b:
        big = a.count(i)
        number = i
        print(big,number)
        #if big == a.count(i) and i not in b:
        b.append(i)
        length +=1
        #else:
         #   pass
'''for i in b:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1
dict1=dict.copy()

for k in dict:
    if dict.get(k) > big:
        big = dict.get(k)
    else:
        dict1.pop(k)'''
        #pass
#       c =
#print(dict)
print(b,length)
if length > 1:
    print(f"There's {length} numbers with same maximum appearances. Choosing the 1st one.")
    for i in b:
        if a.index(i) < a.index(number):
            number = i
        else:
            pass
else:
    pass
print(f"Number {number} appeared {big} times")
#print(dict1)
