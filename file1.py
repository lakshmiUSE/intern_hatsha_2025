#WAP read the data from the file sample.txt and count te number of words.
#And count the c words
#step1:
fobj=open("sample.txt",'r')
data=fobj.read()
fobj.close()
print(data)
#step2:Get the words
words=data.split(' ')
print(words)
#step3
count=len(words)
print(count)
#step4:filter out the words starts with c
cwords=[]
for word in  words:
    if word[0]=='c' or word[0]=='C':
        cwords.append(word)
print(cwords)
print(f"the count of  c words:{len(cwords)} and total:{len(words)}")
