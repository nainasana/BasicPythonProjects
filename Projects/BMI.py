# #Body mass index Project

# height = float(input("Enter the height: ")) 
# weight = float(input("Enter the weight: ")) 

# bmi = weight/ (height ** 2) #formula square root of height

# if bmi < 18.5: #true
#     category = "Underweight" #checked
# elif bmi < 25:
#     category = "Normal weight"
# elif bmi< 30:
#     category = "Overweight"
# else:
#     category = "Obese"
    
# print("Your BMI is: ", round(bmi)) #tells boday mass index
# print("Category: ", category) #shows in what category iam






































height = float(input("Enter your height in meters: ")) 
weight = float(input("Enter your weight in kgs: "))

bmi = weight/(height **2)

if bmi<18.5:
    category = "Underweight"
elif bmi<25:
    category = "Normal weight"
elif bmi<30:
    category = "Overweight"
else:
    category = "Obese"
    
print("Your BMI is: ", round(bmi)) #round() - round the result
print("Catergory: ", category)
    















 