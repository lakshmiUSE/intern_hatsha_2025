# WAP to check professional course eligibility.
marks = float(input("Enter your percentage: "))

if marks >= 85:
    print("Eligible for Engineering and Medical courses")
elif marks >= 70:
    print("Eligible for Engineering courses")
elif marks >= 60:
    print("Eligible for Degree professional courses")
else:
    print("Not eligible for professional courses")
