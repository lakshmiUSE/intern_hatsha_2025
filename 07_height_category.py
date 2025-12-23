# WAP to categorize person based on height.
height = float(input("Enter height in centimeters: "))
if height < 150.0:
    category = "small"
elif height >= 150.0 and height < 165.0:
    category = "Average height"
elif height >= 165.0 and height <= 195.0:
    category = "Taller"
else:
    category = "Abnormal height"
print(f"The person is categorized as: {category}")
