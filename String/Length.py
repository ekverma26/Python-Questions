Q Write a Python function that takes a list of words and returns the length of the longest one.

f_str=input("Enter the list of word separated by comma:")
a_list = f_str.split(",")
def len_log(list1):
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max
print(len_log(a_list))
    
