l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")

for i in range(0,n):
    x=int(input())
    l.append(x)
print("List: ",l)
a=int(input("enter element you want to search:"))
c=0
for i in range(0,len(l)):
    if l[i]==a:
        c=1
if c==0:
    print("element not found")
else:
    print("element found.")
