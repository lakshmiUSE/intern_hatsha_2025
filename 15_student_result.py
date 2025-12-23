# WAP to calculate total, percentage, and division.
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Division: First Division")
elif percentage >= 50:
    print("Division: Second Division")
elif percentage >= 40:
    print("Division: Third Division")
else:
    print("Division: Fail")
