#WAP a program to find the sum of all the numbers which are divisible by 4
x=[450,540,1256,2506,15342,89,76,56,90]
y=[]#place holder to store all the numbers which are divisible by 4
total=0
for e in x:
    if e%4==0:
       y.append(e)
       total=total+e
print(f"given input:{x}")
print(f"elements which  are divisible by 4:{y}")
print(f"sum of elemnets which  are divisible by 4:{total}")
