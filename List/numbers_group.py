Q Write a Python program to generate groups of five consecutive numbers in a list.


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
length=len(l1)
a=[]
i=0
n=1
if length%5==0:
    div=int(length/5)
    a=[[5*i+j for j in range(1,6)]for i in range(div)]
print(a)
        
