Q Write a Python program that reads two integers representing a month and day and prints the season for that month and day.


day=int(input(print("Enter day is numbers:")))
month=int(input(print("Enter month in numbers:")))
if month==3 or month==4 or month==5:
    print("Season is:Spring")
elif month==6 or month==7 or month==8:
    print("Season is:Summer")
elif month==9 or month==10 or month==11:
    print("Season is:Autumn")
else:
    print("Winter")
