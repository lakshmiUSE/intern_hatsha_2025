# WAP to display description based on grade.
grade = input("Enter your grade (A, B, C, D, F): ").upper()

if grade == 'A':
    print("Excellent")
elif grade == 'B':
    print("Good")
elif grade == 'C':
    print("Average")
elif grade == 'D':
    print("Needs improvement")
elif grade == 'F':
    print("Fail")
else:
    print("Invalid grade entered. Please enter a grade between A and F.")
