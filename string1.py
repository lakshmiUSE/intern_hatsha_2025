"""The given string contains both lowercase and uppercase letters in random
order and combines all lowercase letters and displays in output.
Example:  #input :   AmaZOn
	    #output: man"""
#Solution1
word= "AmaZOn"
output=""
for ch in word:
    if ch>="a" and ch<="z":
        output=output+ch
print(output)


#Solution2
word= "AmaZOn"
output=""
for ch in word:
    if ord(ch)>=65 and ord(ch)<=90:
          output=output+ch
print(output)
