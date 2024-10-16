# To calculate the lecture and laboratory grade and convert to GPA
# December 12, 2023
# Ahiezer Dayl P. Dalangin


# Get the laboratory grade
print ("Please enter your laboratory grades. Range (0-100) only.")
while True:
    try: 
        Lab_Quiz = float(input("Laboratory quiz grade: "))
        if Lab_Quiz > 100 or Lab_Quiz < 0:
            print ("Invalid number. Please enter a number within th given range")
        else:
            break
    except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
while True:
    try:
        Lab_Activity = float(input("Laboratory activity grade: "))
        if Lab_Activity > 100 or Lab_Activity < 0:
            print  ("Invalid number. Please enter a number within th given range")
        else:
            break
    except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")    
while True:
    try:
        Lab_Project = float(input("Laboratory project grade: "))
        if Lab_Project > 100 or Lab_Project < 0:
            print  ("Invalid number. Please enter a number within th given range")
        else:
            break  
    except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
while True:
    try:
        Lab_Recitation = float(input("Laboratory recitation grade: "))
        if Lab_Recitation > 100 or Lab_Recitation < 0:
            print ("Invalid number. Please enter a number within th given range")
        else:
            break
    except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
    
while True: 
    try:
        Lab_Exam = float(input("Laboratory exam grade: "))
        if Lab_Exam > 100 or Lab_Exam < 0:
            print  ("Invalid number. Please enter a number within th given range")
        else:
            break  
    except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
            
# Calculate the Laboratory grade
Lab_Grade = (Lab_Quiz*0.25) + (Lab_Activity*0.15) + (Lab_Project*0.15) + (Lab_Recitation*0.10) + (Lab_Exam*0.35)
print ("\nLaboratory Grade:" , Lab_Grade)
    
# Get the grades for lectures
print ("\nPlease enter your lecture grades. Range (0-100) only.")
while True:
    Lec_Quiz = float(input("Lecture quiz grade: "))
    if Lec_Quiz > 100 or Lec_Quiz < 0:
        print ("Invalid number. Please enter a number within th given range")
    else:
        break

while True: 
    Lec_Activity = float(input("Lecture activity grade: "))
    if Lec_Activity > 100 or Lec_Activity < 0:
        print  ("Invalid number. Please enter a number within th given range")
    else:
        break
    
while True: 
    Lec_Project = float(input("Lecture project grade: "))
    if Lec_Project > 100 or Lec_Project < 0:
        print  ("Invalid number. Please enter a number within th given range")
    else:
        break  
    
while True: 
    Lec_Recitation = float(input("Lecture recitation grade: "))
    if Lab_Recitation > 100 or Lab_Recitation < 0:
        print ("Invalid number. Please enter a number within th given range")
    else:
        break  
    
while True: 
    Lec_Exam = float(input("Lecture exam grade:"))
    if Lec_Exam > 100 or Lec_Exam < 0:
        print  ("Invalid number. Please enter a number within th given range")
    else:
        break   

# Calculate the Lecture Grade   
Lec_Grade = (Lec_Quiz*0.25) + (Lec_Activity*0.15) + (Lec_Project*0.15)+ (Lec_Recitation*0.10) + (Lec_Exam*0.35)
print ("\nLecture grade: " , Lec_Grade)

Final_Grade = (Lec_Grade*0.70) + (Lab_Grade*0.30)
print ("\nFinal Grade: ", Final_Grade)
    
 # Convert the GWA to a Grade Point Average
GWA = Final_Grade
if (round (GWA)) > 100:
    print ("Invalid Grade")
elif (round (GWA)) >=97:
    print ("GPA: 1.00 ")
elif (round (GWA)) >= 94:
    print ("GPA: 1.25 ")
elif (round (GWA)) >= 91:
    print ("GPA: 1.50")
elif (round (GWA)) >= 88:
    print ("GPA: 1.75")
elif (round (GWA)) >= 85:
    print ("GPA: 2.00")
elif (round (GWA)) >= 82:
    print ("GPA 2.25")
elif (round (GWA)) >= 79:
    print ("GPA: 2.50")
elif (round (GWA)) >= 76:
    print ("GPA: 2.75")
elif (round (GWA)) == 75:
    print ("GPA: 3.00")
elif (round (GWA)) < 75:
    print ("Invalid. Failing Grade")

# END OF PROGRAM   
    
    
    
    
    
    

