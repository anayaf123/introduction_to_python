# Bevan W . , Multiplying and Dividing Factors, 5/6/2019,version 0.4

print("Hello, My name is Fraction-Bot9000.  I will multiply and divide fractions for you.\n")
user_name = input("What is your name? [Type youe name press ENTER.\n")
print("In order to multiply and divide fractions, I need to know the numerator and denominator.")
print("Hello,", user_name,"how are you today?\n")

print("For this program, I need to know the numerator and denominator for both fractions.\n")

# Varible for fraction 0.
numerator0 = 0
denominator0 = 0


# Varible for fraction 1.
numerator1 = 0
denominator1 = 0
numerator0 = int(input("Type the first numerator and press enter.\n"))
numerator1 = int (input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))


print("When multiplying fractions you multiply the two numerators together .\n")
print ("Then you will multiply the two denominators together.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is",new_numerator,"/", new_denominator,".\n")

# This is where the division of the fractions will start

print("To divide a fraction, you will multiply using recipracol or inverse of the second fraction")

new_2ndnumerator = numerator0 * denominator1
new_2nddenominator = denominator0 * numerator1
print("The new fraction is",new_2ndnumerator,"/", new_2nddenominator,".\n")