Q Write a Python function that prints out the first n rows of Pascal's triangle. 
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

Pascal's triangle
Each number is the two numbers above it added together


n=int(input("Enter no. of rows:"))
l=[]
for i in range(n):
    l.append([])
    l[i].append(1)
    for j in range(1,i+1):
        if j==i:
            l[i].append(1)
        else:
            l[i].append(l[i-1][j-1]+l[i-1][j])
m=n
print(l)
for i in range(len(l)):
    print()
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print(l[i][j],end=" ")
    
