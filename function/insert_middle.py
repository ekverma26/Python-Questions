Q Write a Python function to insert a string in the middle of a string.
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def middle_insert(str1,str2):
    len1=len(str1)
    mid=int(len1/2)
    for i in range(mid):
        print(str1[i],end='')
    print(str2,end='')
    for i in range(mid,len1):
        print(str1[i],end='')
middle_insert('[[]]','Python')
print()
middle_insert("{{}}","PHP")
