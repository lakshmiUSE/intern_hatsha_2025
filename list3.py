#WAP combine all list of strings with hypen(-)

x=["name","harsha","vardhan"]
#name-harsha-vardhan
output=""
for i in range(0,len(x)-1):
    output=output+x[i]
    output=output+"-"
print(output)#+x[len(x)-1])
