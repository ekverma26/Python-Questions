Q Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is.

str=input("Enter a your full name:")
list1=str.split(" ")
print(list1[0][0],list1[1][0],list1[2])
