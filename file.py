#open---read/write/append----close

"""fobj=open("sample.txt",'w')
fobj.write("hello vdac")
fobj.close()"""

"""
fobj=open("sample.txt",'r')
text=fobj.read()
print(text)
fobj.close()"""


fobj=open("sample.txt",'a')
fobj.write("hi all")
fobj.close()
fobj=open("C:\\Users\\bhagy\\OneDrive\\Desktop\\New folder\\sample.txt",'r')
text=fobj.read()
print(text)
fobj.close()
