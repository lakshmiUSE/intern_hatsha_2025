#WAP reverse given list
#x=[10,20,30,40,50]
#note:you should not use list.reverse()function
x=[10,20,30,40,50]
y=[]
print(f"input:{x}")
#traversing a list indexs from last to first
#by range function()
for i in range(len(x)-1,-4,-1):
    y.append(x[i])
print(y)
print(f"output reverse list :{y}")
    

