Q Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2


list1=['abc', 'xyz', 'aba', '1221','1111']
length=len(list1)
j=0
n=0
for i in range(length):
    p=len(list1[i])
    if p>=2:
        if list1[i][0]==list1[i][p-1]:
            n=n+1
print(n)
