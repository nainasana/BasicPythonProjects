# # #Number guessing game

# # import random


# # def guess_number():
# #     secret_number = random.randint(1, 100) #- Taking a  random interger between the range 1- 100
# #     attemps = 0 #initialize
# #     print("Welcome to the Number Guessing Game!")
# #     print("I'm thinking of a number between 1 and 100.")
    
# #     while attemps < 6:
# #         # loop runs or executes continuously till the condition becomes false
# #         guess = int(input("Take a guess: "))
# #         attemps += 1 #=> attemps = attemps + 1 = 0+1 = incrementation and decrementation
        
# #         if guess < secret_number:
# #             print("Too low")
# #         elif guess > secret_number:
# #             print("Too high!")
# #         else:
# #             print("Congratulations! You guessed the number in", attemps, "attemps!")

# #             break 
    
# #     if attemps == 6:
# #         print("Sorry, your chances are completed. The number was", secret_number)
        
# #     play_again = input("Do you want to play again? (yes/no): ")
# #     if play_again.lower() == "yes":
# #         guess_number()
# #     elif play_again.upper() == "yes":
# #         guess_number()
# #     else:
# #         print("Thank you for playing the Number Guessing Game!")
        
# # guess_number()




# import random

# def guess_number():
#     secret_number = random.randint(1,100)
#     attempts = 0 #initialization
    
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100")
    
#     while attempts < 6:
#         guess = int(input("Take a guess: "))
#         attempts += 1
        
#         if guess < secret_number:
#             print("Too low! Try again")
#         elif guess > secret_number:
#             print("Too high!")
#         else:
#             print("Congratulations! You guessed the number in", attempts, "attempts!")
            
#             break
        
#     if attempts == 6:
#         print("Sorry, your chances are completed. The number was",secret_number)
        
#     play_again = input("Do you want play again? (yes/no): ")
    
#     if play_again.lower() == "yes":
#         guess_number()
#     elif play_again.upper() == "yes":
#         guess_number()
#     else:
#         print("Thank you for playing the Number Guessing Game!")
    
# guess_number()        
        


#Number guessing game 

import random

def guess_number():
    secret_number = random.randint(1,100)
    attempts = 0 #inintialization
    
    print("Welcome to the Number Guessing Game")
    print("Iam guessing a number between 1-100")
    
    while attempts < 6 : #condition
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts")
            
            break
        
    if attempts == 6:
        print("Sorry, your chances are completed. The number is:", secret_number)
        
        
    play_again = input("Do you want to play again? (yes/no)")
    
    if play_again.lower() == "yes":
        guess_number()
    elif play_again.upper() == "yes":
        guess_number()
    else:
        print("Thankyou for playing the Number Guessing Game")
    
guess_number()












