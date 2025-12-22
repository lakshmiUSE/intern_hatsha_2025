"""combine all the characters from the given sentence which the
respective indices are divisible by 5 and ignore the space in output"""
#input:Winners are not those who never fail but those who never quit
#expected output:Wreerlert
sen="Winners are not those who never fail but those who never quit"
res=""
for i in range(0,len(sen)):
    if i%5==0:
        if sen[i] !=' ':
            res=res+sen[i]
print(res)
