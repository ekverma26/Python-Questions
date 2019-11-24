Q. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
bd

dict3={}
str1="w3resource"
for n in str1:
    keys=dict3.keys()
    if n==keys:
        dict3[n]+=1
    else:
        dict3[n]=1
print(dict3)
