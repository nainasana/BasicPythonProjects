# #Day of the week project

day_number = input("Enter a number from 1 to 7: ") 

#Check if the input is a valid number between 1 and 7
if day_number.isdigit():  #true        #isdigit() method will check if the input given by the user is a digit or not.
    day_number = int(day_number)   #if the user enter a digit. That digit will ge6t stored as an interger in the variable day_number
    if day_number >=1 and day_number <=7: #The input entered by the user is bewteen the number 1 and 7
        if day_number == 1: 
            day = "Monday" 
        elif day_number == 2:
            day = "Tuesday" 
        elif day_number == 3: 
            day = "Wednesday" 
        elif day_number == 4:
            day = "Thursday" 
        elif day_number == 5:
            day = "Friday" 
        elif day_number == 6: 
            day = "Saturday" 
        elif day_number == 7: 
            day = "Sunday" 
        
        print("The day of the week is: ", day)
            
    else:
        print("Invalid input. Please enter a number from 1 to 7.")
else:
    print("Invalid input. Please enter a number.") #string, space
    
    
    











