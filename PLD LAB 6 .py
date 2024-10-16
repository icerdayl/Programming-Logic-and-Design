# Create a program that will generate 3 different star patterns
# Dalangin, Ahiezer Dayl P.
# January 15, 2024

# Choose a specific star pattern
while True:
    while True:
        try:
            print("\nCHOOSE A STAR PATTERN!!!")
            print("Type....")
            print("1 - Left sided star pattern")
            print("2 - Right sided star pattern")
            print("3 - Left and right sided star pattern")
            print("4 - Exit the program\n")
            pattern = int(input("Choose a number: "))
            if pattern == 4:
                exit ("\nYou chose to end the program. Thank you.")
            elif pattern >= 5 or pattern <= 0:
                print ("\nINVALID INPUT! Choose a number ranging only from 1 - 4")
            else:
                break
        except ValueError:
            print ("\nINVALID CHARACTER! Input a number only.")
# Number of rows
    n = 5

# Left sided star pattern           
    if pattern == 1:  
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(n):
            for j in range(i,n-1):
                print("*", end="")
            print()
# Right sided star pattern
    elif pattern == 2: 
        for i in range(n):
            for j in range(i, 4):
                print(" ", end="")
            for k in range(i + 1):
                print("*", end="")
            print()
        for i in range(n-1):
            for j in range (i + 1):
                print(" ", end="")
            for k in range(i, 4):
                print("*", end="")
            print()
# Left and right star pattern            
    elif pattern == 3:  
        for i in range(4):
                for j in range(i + 1):
                    print("*", end="")
                for j in range((i % 4) + i, 7):
                    print(" ", end="")
                for j in range(i + 1):
                    print("*", end="")
                print()

        for i in range(4, -1, -1):
                if i == 4:
                    print("*" * 9)
                else:
                    for j in range(i + 1):
                        print("*", end="")
                    for j in range((i % 4) + i, 7):
                        print(" ", end="")
                    for j in range(i + 1):
                        print("*", end="")
                    print()
# Try Again prompt
    while True:
        tryAgain = input("\nDo you want to try again? (Yes/No): ")
    
        if tryAgain.upper() == "YES":
            break
        elif tryAgain.upper() == "NO":
            exit ("\nYou chose to end the program. Thank you.")
        else:
            print ("\nINVLID INPUT! Answer only with Yes/No. ")
            
# End of program

