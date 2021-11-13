class User:
 def __init__(self, name, pin, password):
  self.name = name
  self.pin = pin
  self.password = password

 def to_string(self):
   print(self.name, self.pin, self.password)

 def change_name(self):
  self.name = input("Please enter a new name.")
  print("Your updated name is " + self.name)

 def change_pin(self):
    self.pin = input("Please enter a new pin.")
    print("Your updated pin is " + str(self.pin))

 def change_password(self):
    self.password = input("Please enter a new password.")
    print("Your updated name is " + str(self.password))

#Task 3
class BankUser(User):
 def __init__(self, name, pin, password): 
  super().__init__(name, pin, password)
  self.balance = 0

 def show_balance(self):
   print(self.name + "'s Balance is: " + str(self.balance))
 
 def withdraw(self, amount):
   amount = float(input("Hi " + self.name + " How much would you like to withdraw?"))
   self.balance -= amount

 def deposit(self, amount):
   amount = float(input("Hi " + self.name + " How much would you like to deposit?"))
   self.balance += amount
 
 def to_string(self):
   print(self.name, self.pin, self.password, self.balance)

 def transfer_money(self, user, amount):
  print("You are transferring $" + str(amount), "to", user.name)
  print("Authentication required")
  pincode = int(input("Enter your PIN: "))
  if pincode != self.pin:
    print("Invalid PIN. Transaction canceled.")
    return False
  else:
    print("Transfer authorized")
    print("Transferring $" + str(amount) + " to " + user.name)
    self.balance -= amount
    user.balance += amount

  return True

 def request_money(self, user, amount):
  print("You are requesting $" +
              str(amount), "from", user.name)
  print("User authentication is required...")

  pin = int(input("Enter " + user.name + "'s PIN: "))
  if pin != user.pin:
    print("Invalid PIN. Transaction canceled.")
    return False

  password = input("Enter your password: ")
  if password != self.password:
    print("Invalid password. Transaction canceled.")
    return False
  else:
    print("Request authorized")
    print(user.name + " sent $" + str(amount))

    user.balance -= amount
    self.balance += amount

    return True
 
 
 
 
 
 
 
 
""" Begin Driver Code for Task 1 
#test_user = User("Bob", 1234, "password")

When you call a method associated with an object self is supplied by default.
Which is why there are no arguments necessary on line 22.
test_user.to_string()
"""
""" End Driver Code for Task 1 """
""" Begin Driver Code for Task 2 
test_user = User("Bob", 1234, "password")
test_user.to_string()
test_user.change_password()
test_user.to_string()
test_user.change_name()
test_user.to_string()
test_user.change_pin()
test_user.to_string()
"""
""" End Driver Code for Task 2 """

""" Begin Driver Code for Task 3 
test_bank_user = BankUser("Bob", 1234, "password")
test_bank_user.to_string()
"""
""" End Driver Code for Task 3 """

""" Begin Driver Code for Task 4
bank_user_1 = BankUser("Bob", 1234, "password")
bank_user_1.show_balance()
bank_user_1.deposit()
bank_user_1.show_balance()
bank_user_1.withdraw()
bank_user_1.show_balance()
 """
""" End Driver Code for Task 4 """
""" Begin Driver Code for Task 5"""
bank_user_1 = BankUser("Bob", 1234, "password")
bank_user_2 = BankUser("Terrance", 1234, "password")
bank_user_2.deposit(5000)
bank_user_2.show_balance()
bank_user_1.show_balance()
print()

bank_user_2.transfer_money(bank_user_1, 500)
bank_user_1.show_balance()
bank_user_2.show_balance()
print()

bank_user_2.request_money(bank_user_1, 250)
bank_user_1.show_balance()
bank_user_2.show_balance()
""" End Driver Code for Task 5"""