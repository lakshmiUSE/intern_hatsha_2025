#WAP a program combine all first charcters from the given list of strings
#x=["python","java","cpp","go"]
#output:"pjcg"
x=["python","java","cpp","go"]
y=""
for word in x:
    #print(word[0])
    y=y+word[0]
print(f"Output:{y}")
