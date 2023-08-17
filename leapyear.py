#print("")
year = int(input("Enter Year\n"))

if ( year % 4 == 0 ):
    if ( year % 100 == 0 ):
        if ( year % 400 == 0 ):
            print("Year is leap year")
        else:
            print("Not leap year")
    else:
       print("Leap year") 
else:
    print("Not leap year")
