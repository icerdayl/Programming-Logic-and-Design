def bounds(value, lower_bound, upper_bound):
    return lower_bound <= value <= upper_bound
    
while True:
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    if lower_bound > upper_bound:
        print("Sum: 0 (Lower bound should have less value than the higher bound.)")
        continue
    
    total_sum = 0
    while True:
        value = int(input("Enter a value (negative to stop): "))
        if value < lower_bound or value > upper_bound:
            print ("Please enter a value within the indicated bounds only")
            break
        
        if value < 0:
            break
        if bounds(value, lower_bound, upper_bound):
            total_sum += value

    print("Sum within bounds:", total_sum)
    
    try_again = input("Do you want to try again (Y/N): ").upper()
    if try_again != 'Y':
        exit ("Program ended")

