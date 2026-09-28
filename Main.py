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
class Bank_Account:
    def __init__(self, name, phone_number, balance, password):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.password = password
    
    def deposit(self):
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("Enter valid amount!")
        self.balance += amount
    
    def withdraw(self):
        amount = int(input("Enter amount: "))
        if amount > self.balance or amount < 0:
            print("Enter valid amount!")
        self.balance -= amount
    
    def show_info(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.balance}")
        
        
    
b1 = Bank_Account("Clarence", 123, 100, 'Password1')
b1.show_info()

