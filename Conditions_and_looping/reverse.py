Q Write a Python program that accepts a word from the user and reverse it.

word=input("Enter a word:")
for i in range(len(word)-1,-1,-1):
    print(word[i],end="")
print("\n")
