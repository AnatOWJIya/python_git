<<<<<<< HEAD:most_frequent_number.py
a = [int (x) for x in input("Enter  number sequence:\n").split()]
b = sorted(a)
dict = {}
big = 1
for i in b:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1
dict1=dict.copy()
for k in dict:
    if dict.get(k) > big:
        big = dict.get(k)
    else:
        dict1.pop(k)
print(dict)
print(dict1)
=======
a = [int (x) for x in input("Enter  number sequence:\n").split()]
b = sorted(a)
dict = {}
big = 1
for i in b:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1
dict1=dict.copy()
for k in dict:
    if dict.get(k) > big:
        big = dict.get(k)
    else:
        dict1.pop(k)
print(dict)
print(dict1)
>>>>>>> ef90de75f883a687ad6ff5d26af5bf645af1b749:most_frequent_number.py
