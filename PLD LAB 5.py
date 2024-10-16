# Determine the number of values and the sum of odd and even numbers
# January 4 2024
# Ahiezer Dayl P. Dalangin
while True:
    while True:
        try:
            numbers = int(input("Please enter how many numbers you want to enter: "))
            if numbers <= 0:
                print("Please enter a positive number")
            else:
                break
        except ValueError:
            print("Invalid Input. Please enter a whole number.")
    term = 1
    sum_even = 0
    sum_odd = 0
    
# Check if the term equates to the entered numbers
# Solve and present the sum of odd and even numbers
    while term <= numbers:
        try:
            value = int(input(f"Enter number {term}: "))
            if value % 2 == 0:
                sum_even = sum_even + value
            else:
                sum_odd = sum_odd + value
            term = term + 1
        except ValueError:
            print("Please input a number.")

    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")
    
 
    while True:
        loop=(input("Do you want another attempt? Please answer with Yes or No: "))
        if loop=="Yes" or loop=="yes":
            break
        elif loop =="No" or loop == "no":
            exit ("You answered no. The program will terminate. Thank you")
        else:
            print("Please answer only with Yes or No.")
            continue

# End of Program
        
    

