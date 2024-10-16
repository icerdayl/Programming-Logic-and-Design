# Enter a number and a character. If the character is "C", it will display the cube of the number and if "S", display the square of the number
# January 11, 2024
# Ahiezer Dayl P. Dalangin

# Enter the number and the character and solve the number
num = int(input("Please enter a number: "))

character = input("Choose a letter between S or C: ")
if character == "S":
    print ("Answer: ", num**2)
elif character == "C":
    print ("Answer: ", num**3)
else:
    print ("INVALID CHARACTER!")
    
#End of program

   
