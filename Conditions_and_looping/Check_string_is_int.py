text=input("Enter a text:")
text=text.strip()
print(text)
if all(text[i] in "0123456789" for i in range(len(text))):
    print("Integer")
elif (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1,len(text))):
    print("Integer")
else:
    print("Not an integer")
