# Using if / else Statements, Ryan Kelley, February 05, 2020.  Version 0.25


import random # This is a special library built-in to Python.  It has special methods, in this case .shuffle() that I will use in this code. 
import time # This lets us call the sleep() method which pauses the program for a specified number of seconds.

print("""
   __    __       _______. __  .__   __.   _______                                                                 
  |  |  |  |     /       ||  | |  \ |  |  /  _____|                                                                
  |  |  |  |    |   (----`|  | |   \|  | |  |  __                                                                  
  |  |  |  |     \   \    |  | |  . `  | |  | |_ |                                                                 
  |  `--'  | .----)   |   |  | |  |\   | |  |__| |                                                                 
   \______/  |_______/    |__| |__| \__|  \______|                                                                 
   __   _______         ___    _______  __           _______. _______                                              
  |  | |   ____|       /  /   |   ____||  |         /       ||   ____|                                             
  |  | |  |__         /  /    |  |__   |  |        |   (----`|  |__                                                
  |  | |   __|       /  /     |   __|  |  |         \   \    |   __|                                               
  |  | |  |         /  /      |  |____ |  `----..----)   |   |  |____                                              
  |__| |__|        /__/       |_______||_______||_______/    |_______|                                             
       _______..___________.    ___   .___________. _______ .___  ___.  _______ .__   __. .___________.    _______.
      /       ||           |   /   \  |           ||   ____||   \/   | |   ____||  \ |  | |           |   /       |
     |   (----``---|  |----`  /  ^  \ `---|  |----`|  |__   |  \  /  | |  |__   |   \|  | `---|  |----`  |   (----`
      \   \        |  |      /  /_\  \    |  |     |   __|  |  |\/|  | |   __|  |  . `  |     |  |        \   \    
  .----)   |       |  |     /  _____  \   |  |     |  |____ |  |  |  | |  |____ |  |\   |     |  |    .----)   |   
  |_______/        |__|    /__/     \__\  |__|     |_______||__|  |__| |_______||__| \__|     |__|    |_______/    
                                                                                                                   
                                       by Ryan Kelley, February 05, 2020 Version 0.25
""")
time.sleep(2) 
print("Hello $user, this program will help you learn how to use if / else statements in your code.  If you have any questions while using this program please raise your hand.\n")
user0 = str(input("$user, by what name should I call you?  Please, type your firt and last name and then press ENTER on your keyboard.\n")) # Create a variable named user and assign it a value.
# In Python, = is the English equivalent of "Make the thing on the left have the same value as the thing on the right."  


# The following lines of code create three slices of the user name and then rearranges them. 
user1 = user0[0:3]
user2 = user0[4:7]
user3 = user0[8:len(user0)]
user4 = user3 + user2 + user1

print("Your parents really named you",user4,"?\n")
time.sleep(2) 
name_correct = input("Is what really what I should call you?  [Yes/No?]\n") # Create the variable name_correct and assign it a value. 
name_correct = name_correct[0] # This assigns the name_correct variable to JUST the first letter of the user's answer. 
name_correct = str.lower(name_correct) # This assigns the name_correct variable to the lower case version of that first letter.
# It works! print(name_correct)

# Our first if / else statement starts here.  It will check the VALUE of the name_correct variable and then test it against each CONDITION.

if name_correct == "y": # == is the English equivalent of "Is the thing on the left the same as the thing on the right?"
    # If they answer yes just leave user0 variable alone and continue on in the program.
    print("Ok, ",user0,"it is!\n")
elif name_correct == "n":
    # On the next line we will have the user re-type their name.  
    user0 = str(input("I am sorry.  I experienced a memory error in one of my circuits.  Please retype your name and press enter.\n"))
    print("Ahh! Yes,",user0,"that's more like it!\n")

elif dice_roll == 3:
    print("Squeal with glee, you got a three!\n")
    print("Please get a Cherry Jolly Rancher.\n") 
elif dice_roll == 4:
    print("Jump off the floor, the die says four!  \n")
    print("Please get a Grape Jolly Rancher.\n") 
elif dice_roll == 5:
    print("You rolled a five, that's no jive!\n")
    print("Please get a Water Melon Jolly Rancher.\n")
else:
    print("You rolled a six, please take your pick!  Get any flavor Jolly Rancher you would like.\n")

    



