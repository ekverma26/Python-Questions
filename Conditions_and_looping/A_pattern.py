Q Write a Python program to print alphabet pattern 'A'. 
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *

r_str=""
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3) and (col>0 and col<4)) or ((col==0 or col==4) and (row>0 and row<7)):
            r_str=r_str+"*"
        else:
            r_str=r_str+" "
    r_str=r_str+"\n"       
print(r_str)
