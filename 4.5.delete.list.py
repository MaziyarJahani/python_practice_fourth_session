user_list = []
print("please enter your numbers, when it ends, enter: exit")
while True:
    b = input("please enter your number:")
    if b == "exit":
        print("your list is:", user_list)
        break
    else:
        user_list.append(b)
#user_list = list(map(int, user_list))
new_list = []
for i in user_list:
    if i not in new_list:
        new_list.append(i)
print("your new list is:",new_list)
#user_list = [2, 3, 6, 7, 7, 14, 2, 7]
#new_list = list(set(user_list))
#print(new_list)