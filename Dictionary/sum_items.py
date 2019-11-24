Q. Write a Python program to sum all the items in a dictionary.

dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
sum=0
item=dict1.values()
#print(item)
for i in item:
    sum=sum+i
print(sum)
