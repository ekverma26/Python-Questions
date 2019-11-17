Q Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


l1=['p','q']
l2=[]
for i in range(1,6):
    for j in range(len(l1)):
        p=l1[j]+str(i)
        l2.append(p)
print(l2)
