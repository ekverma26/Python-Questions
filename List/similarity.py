'''Q Write a Python program to compute the similarity between two lists. 
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output: 
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']'''


l1=["red", "orange", "green", "blue", "white"]
l2=["black", "yellow", "green", "blue"]
print(list(set(l1)-set(l2)))
print(list(set(l2)-set(l1)))
