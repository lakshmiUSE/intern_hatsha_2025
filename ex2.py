#WAP find sum of all the  numbers which are divisible by 5

x=[1,15,67,65,90,87,95,45]
s=0
for e in x:
    if e%5==0:
        s=s+e
print(s)
    
