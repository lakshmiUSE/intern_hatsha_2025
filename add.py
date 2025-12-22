#WAP find sum of all the numbers which are divisible by 5
x=[10,16,15,18,85,54,73]
s=0
for e in x:
    if e%5 ==0:
        s=s+e
print(s)
