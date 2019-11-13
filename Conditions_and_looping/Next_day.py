Q Write a Python program to get next day of a given date.
Expected Output:
	
Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24  


yr=int(input(print("Enter year in numbers:")))
mt=int(input(print("Enter month in numbers:")))
day=int(input(print("Enter day in numbers:")))
if yr%4!=0:
    if (day<31 and mt!=2) or (mt==2 and day<28):
        print(yr,"-",mt,"-",day+1)
    else:
        print(yr,"-",mt+1,"-",1)
else:
    if (day<31 and mt!=2) or (mt==2 and day<29):
        print(yr,"-",mt,"-",day+1)
    else:
        print(yr,"-",mt+1,"-",1)
