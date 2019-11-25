Q Write a Python function that checks whether a passed string is palindrome or not.


def palin(str1):
    list1=list(str1)
    l=len(list1)-1
    list2=[]
    j=0
    for i in range(l,-1,-1):
        list2.append(list1[i])
        j=j+1
    if list1==list2:
        print("Palindrom")
    else:
        print("Not palindrom")
s=input("enter string:")
palin(s)
