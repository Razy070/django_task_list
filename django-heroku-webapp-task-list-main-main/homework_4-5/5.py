# login, password = input("Enter login and password: ")
# if login == "user" and password == "qwerty":
#     print("Authentication completed")
# else:
#     print("Invalid login or password")


##########################################################

summ = float(input("Insert amount in KZT:\n"))

curr = int(input("[1] USD\n[2] EUR\n[3] RUB\n "))
if curr == 1:

    print(f"{round(summ / 420, 2)} USD")
elif curr == 2:
    print(f"{round(summ / 510, 2)} EUR")
elif curr == 3:
    print(f"{round(summ / 5.8, 2)} RUB")
else:
    print("Invalid currency")
