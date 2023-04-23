import qrcode

name = input("please enter your name:")
phone_number = input ("please enter your phone number:")
x = "Hello, I'm " + name + ", my phone number is "+ phone_number
qrc = qrcode.make (x)
qrc.save ("name and phone qrcode.png")
