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
    def __init__(self, name):
        self.name = name
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def list_users(self):
        return [f"{user.name} {user.phone_number}" for user in self.users]

    
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
        
user1 = BankUser("Michael", 123, 100, "password1")
user2 = BankUser("Franklin", 222, 200.50, "passwordF")

Bank1 = Bank("CO Bank")
Bank1.add_user(user1)
Bank1.add_user(user2)

print(Bank1.list_users())

