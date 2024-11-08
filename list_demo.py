#list is a collection which is ordered and changeable.
# Allows duplicate members.
# The lists are ordered.
# The element of the list can access by index.
# The lists are the mutable type.
# The lists are  mutable type.
# A list can store the number of various elements.
mylist = ["Oil","Saop",123,"Oil","Kurkure","Dairy-milk"]
print(mylist)
print(type(mylist))
print(mylist[0])

#slicing list elements
print(mylist[1:1])
print(mylist[2:5])
# You can use negative index as well
print(mylist[-1])
print(mylist[-2])

for i in mylist:
 print(i,end=" ")