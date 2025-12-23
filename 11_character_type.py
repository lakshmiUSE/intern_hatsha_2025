# WAP to check whether character is alphabet, digit, or special character.
ch = input("Enter a character: ")

if ch.isalpha():
    print("It is an Alphabet")
elif ch.isdigit():
    print("It is a Digit")
else:
    print("It is a Special Character")
