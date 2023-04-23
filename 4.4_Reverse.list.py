user_list = []
print("please enter your numbers, when it ends, enter: exit")
while True:
    b = input("please enter your number:")
    if b == "exit":
        print("your main list is:", user_list)
        break
    else:
        user_list.append(b)
reverse_list = []
for i in range (len(user_list) -1 , -1 , -1):
    reverse_list.append(user_list[i])
print("your reverse list is:" , reverse_list)