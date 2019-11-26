Q Write a Python function to check whether a string is a pangram or not. 
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

def pangram(str1):
    str1=list(str1)
    print(str1)
    count=0
    alph="abcdefghijklmnopqrstuvwxyz"
    l1=list(alph)
    l2=[]
    flag=0
    print(l1)
    for i in l1:
        for j in str1:
            #print(i)
            #print(j)
            if i == j and j!=' ':
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            break
    if (flag==0):
        print("yes string is pangram")
    else:
        print("no")
        
s=input("enter string")
pangram(s)
