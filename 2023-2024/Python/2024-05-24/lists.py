#adrian heredia
#2024-05-08

#creating a empty list
Lst =[]

#using a for loop to add the numbers 1-100 to the list
for a in range(1,101):
    Lst.append(a)

#printing the list lst
print(Lst)

#creating a list named odd
odd =[]

#using a for loop to add the odd numbers 1-100 to the list odd
for b in range(1,101,2):
    odd.append(b)

#printing the list odd
print(odd)

#creating a list named even
even=[]

#using a loop to add even numbers 1-100
for c in range(2,101,2):
    even.append(c)

#printing the list even
print(even)

#create a varlble named B= that points to the first list that you  created
b=Lst

#create a varlbe named joined that joins the even odd lists using a  opperator
joined=even+odd

#output the varibel join
print(joined)

#output the type of the varbel join
print(type(joined))

#comapre the list b to the list joined using  postional comparaison
print(b==joined)