l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")
for i in range(0,n):
    x=int(input())
    l.append(x)
print("List: ",l)
a=int(input("enter element you want to search:"))
c=0

def bs(l,n,a):
    lb=0
    ub=len(l)
    while(lb<ub):
        mid=int((lb+ub)//2)
        if l[mid]>a:
            ub=mid
        elif l[mid]<a:
            lb=mid+1
        else:
            return mid
    return -1

r=bs(l,n,a)

if r==-1:
    print("element not found.")
else:
    print("element found at position:",r+1)


