#Task 4
def show_balance(balance):
 print(balance)
def deposit(balance):
 amount = input("Enter amount to deposit: ")
 return(balance + float(amount))
def withdraw(balance):
 amount = input("Enter amount to withdraw: ")
 return(balance - float(amount))
def logout(name):
 print("Goodbye" + name)