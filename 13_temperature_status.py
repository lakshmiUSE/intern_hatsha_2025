# WAP to display temperature status.
temp = float(input("Enter temperature in °C: "))

if temp < 0:
    print("Freezing weather")
elif temp >= 0 and temp < 20:
    print("Cold weather")
elif temp >= 20 and temp < 30:
    print("Normal temperature")
elif temp >= 30 and temp < 40:
    print("Hot temperature")
else:
    print("Very hot temperature")
