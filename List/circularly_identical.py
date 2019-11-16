Q  Write a python program to check whether two lists are circularly identical.


l1=[10,10,10,0,0]
l2=[10,10,0,10,10]
l3=[]
flag=0
len1=len(l1)
len2=len(l2)
if len1==len2:
    for i in range(len1):
        l3=[]
        count=0
        for j in range(i+1,len1):
            l3.append(l1[j])
        for x in range(i+1):
            l3.append(l1[x])
        for y in range(len1):
            if l2[y]==l3[y]:
                count+=1
        if count==len1:
            flag=1
            break
    if flag==1:
        print("Circular")
    else:
        print("Not circular")
