import time
import json, csv
'''
v1 user class - user,balance,deposit,withdraw
v2 new class : bank - multiple users
v3 bank - registration
v4 bank - log in, auth
v5 file storage, save_users, load_users
v6 user - transactions -- type, amount, date
v7 error handling
'''


class Bank:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)

    
class BankUser():
    def __init__(self, name : str, phone_number : str, balance : float, password : str):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.password = password
        


    def deposit(self):
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Enter valid amount!")
        else:
            self.balance += amount
    
    def withdraw(self):
        amount = float(input("Enter amount: "))
        if amount > self.balance or amount < 0:
            print("Enter valid amount!")
        else:
            self.balance -= amount
    
    def show_info(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.balance}")
        

u1 = BankUser("Michael", 123, 100, 'Password1')
u2 = BankUser("Hasan", 124, 200, "password2")
b1 = Bank()
b1.add_user(u1)
b1.add_user(u2)
print(b1.users[0].name)
print(b1.users[1].name)


 

