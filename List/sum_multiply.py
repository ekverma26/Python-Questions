Q Write a Python program to sum and multiplies all the items in a list.

list1=[1,1,1]
length=len(list1)
sum=0
mul=1
for i in range(length):
    sum=sum+list1[i]
    mul=mul*list1[i]
print("Sum of list is:",sum)
print("Multiplication of list is:",mul)
