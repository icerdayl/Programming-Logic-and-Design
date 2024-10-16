# To compute the final grade of the student
# November 28, 2023
# Ahiezer Dayl P. Dalangin

Lecture_grade = float(input("Please enter your grade in lecture: "))
Lab_grade = float(input("Enter your grade in laboratory: "))

# solve for the final grade
Final_Grade = (Lecture_grade*0.70) + (Lab_grade*0.30)

# display the final grade
print ("Your final grade is: " , Final_Grade)
