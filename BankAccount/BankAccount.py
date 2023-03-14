# Author: Zoey Vail

class BankAccount:
     def __init__(self, account_name, starting_balance):
          self.account_name = account_name
          self.starting_balance = starting_balance
     def deposit_balance(self, deposit):
          self.starting_balance += deposit
     def withdraw_balance(self, withdraw):
          self.starting_balance -= withdraw
     def get_balance(self):
          return self.starting_balance