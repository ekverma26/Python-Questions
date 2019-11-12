Q5 Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

str1=input()
num=str1.split(',')
print(num)
for p in num:
    x = int(p, 2)
    if x%5==0:
        print(p)
