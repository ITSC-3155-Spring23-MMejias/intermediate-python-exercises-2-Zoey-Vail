# Author: Zoey Vail

from BankAccount import BankAccount

myAcc = BankAccount("Zoey", 1200)
deposit = int(input("Enter an amount to deposit: "))
myAcc.deposit_balance(deposit)
withdraw = int(input("Enter an amount to withdraw: "))
myAcc.withdraw_balance(withdraw)
print("Balance: ", myAcc.get_balance())