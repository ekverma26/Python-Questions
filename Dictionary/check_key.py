Q. Write a Python script to check if a given key already exists in a dictionary.

dict4={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n=int(input("Enter a key:"))
count=0
keys1=dict4.keys()
print(keys1)
for i in keys1:
    if i==n:
        count=count+1
if count>0:
    print("key already exists in a dictionary")
else:
    print("key already not exists in a dictionary")
    
