Q To print the following patterns.
 Expected Output:

  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 **** 
 
 ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo 


r_str=""
for row in range(7):
    for col in range(5):
        if (((row==0 or row==3 or row==6) and (col>0 and col<4)) or ((col==0) and (row==1 or row==2 or row==6)) or ((col==4) and (row==0 or row==4 or row==5))):
            r_str=r_str+"*"
        else:
            r_str=r_str+" "
    r_str=r_str+"\n"
print(r_str)

r_str=""
for row in range(15):
    for col in range(17):
        if (((row>=0 and row<3) or (row>5 and row<9) or (row>11 and row<15)) and (col>3 and col<13)) or ((col>=0 and col<4) and ((row>=0 and row<9) or (row>11 and row<15))) or ((col>12 and col<17) and ((row>=0 and row<3) or (row>5 and row<17))):
            r_str=r_str+"o"
        else:
            r_str=r_str+" "
    r_str=r_str+"\n"
print(r_str)
