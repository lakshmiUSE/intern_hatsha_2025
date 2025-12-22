#traffic signals
#r-stop
#g-go
#y-start
#invalid signal

signal=input("input signals: 1-red, 2-green, 3-yellow: ")

if signal=="1":
    print("please stop!")
elif signal=="2":
    print("please go")
elif signal=="3":
    print("please start")
else:
    print("invaild signal")

