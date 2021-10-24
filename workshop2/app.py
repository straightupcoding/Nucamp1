from banking_pkg.account import deposit, logout, withdraw, show_balance
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#Task 2: Registration
print("=== Automated Teller Machine ===")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0

print(name + " has been registered with a starting balance of $" + str(balance))
#End Task 2

#Task 3
while True:
    print("Please Login")
    entered_name = input("Enter Name: ")
    entered_pin = input("Enter PIN: ")
    if entered_name != name:
        print("Invalid credentials!")
    else:
        print("Login successful!")
        break

while True:
    atm_menu(entered_name)
    option = (input("Please choose an option."))

    if int(option) == 1:
        show_balance(balance)
    elif int(option) == 2:
        balance = deposit(balance)
        show_balance(balance)
    elif int(option) == 3:
        balance = withdraw(balance)
        show_balance(balance)
    elif int(option) == 4:
        logout(name)
        break
    else:
        print("Invalid Response")

#End Task 3