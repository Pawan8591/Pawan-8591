t1 =("Adiya",35,78,"O grade")
print(type(t1))
print(t1)

# tuple Slicing
print(t1[1:])
print(t1[:3])
print(t1[1:3])

print(t1[:])

# find lenght of the tuple
print("The length of the tuple is:",len(t1))

# you can also give negative indexing
print(t1[-2])
print(t1[-1])
# Note:
# List is a collection which is odered and changeable .
# List Allows duplicate members.
# Tuple ia a collection which is odered and unchangeable.
# Tuple Allows duplicate members.
t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)

'''
Unordered: Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable:Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Note: Once a set is created, you cannot change its items, but you can remove items and add new items.
Duplicates Not Allowed:
Sets cannot have two items with the same value.
'''
thisset={"apple", "banana", "cherry", "apple"}

print (thisset)

thisset={"apple", "banana", "cherry", True, 1, 2}
thisset ={"apple", "banana", "cherry", True, 1, 2}

print (thisset)

print (len(thisset))

setl= {"apple", "banana", "cherry"}

set2 =(1, 5, 7, 9, 3)

set3 ={True, False, False}

print (setl) print (set2)

print (set3)

weekdays = {"Sun", "Mon", "Tue", "wed", "thurs","fri"}

print(weekdays)