# Using if / else Statements, Ryan Kelley, February 04, 2020.  Version 0.15

import random # This is a special library built-in to Python.  It has special methods, in this case .shuffle() that I will use in this code. 

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
                                                                                                                   
                                       by Ryan Kelley, February 04, 2020 Version 0.15
""")
print("Hello $user, this program will help you learn how to use if / else statements in your code.\n  If you have any questions while using this program please raise your hand.\n")
user0 = str(input("$user, by what name should I call you?  Please, type your name and then press ENTER on your keyboard.\n")) # Create a variable named user and assign it a value.
# In Python, = is the English equivalent of "Make the thing on the left have the same value as the thing on the right."  


# The following lines of code create three slices of the user name and then rearranges them. 
user1 = user[0:3]
user2 = user[4:7]
user3 = user[8:]
user4 = user3 + user2 + user1

print("Your parents really named you",user4,"?\n")
name_correct = input("Is what really what I should call you?  [Y/N?]\n") # Create the variable name_correct and assign it a value. 
name_correct = name_correct[0] # This assigns the name_correct variable to JUST the first letter of the user's answer. 
name_correct = str.lower(name_correct) # This assigns the name_correct variable to the lower case version of that first letter.
# It works! print(name_correct)

# Our first if / else statement starts here.  It will check the VALUE of the name_correct variable and then test it against each CONDITION.
if name_correct == "y": # == is the English equivalent of "Is the thing on the left the same as the thing on the right?"
    print("Ok, ",user,"it is!\n")
elif name_correct == "n":
    print("I am sorry.  I experienced a memory error in one of my circuits.  Please retype your name and press enter.\n")
    user = str(input())
    print("Ahh! Yes,",user,"that's more like it!\n")
else:
    print("Something has caught fire.  Emergency!  Prepare for crash.  Restart the program please.\n")  
    

