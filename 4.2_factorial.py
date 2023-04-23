x = int(input("please enter your number:"))
f = 1
for i in range (1,x+1):
    f = f*i
    if f == x:
        print("yes")
        break
else:
    print("no")
