"""
Author: Dietmar
Date: 18.12.2021
"""



class Account:
    Max_amount=1500
    def __init__(self, owner, bank_account, bank_balance, max_amount=1500):
        self.Owner=owner
        self.Bank_account=bank_account
        self.Bank_balance=bank_balance
        self.Max_amount=max_amount
        self.Max_day=0
    def deposit(self, amount):
        if amount < 0 or self.Max_day+amount >self.Max_amount:
            return print("Einzahlung nicht möglich. Der Betrag: ", self.Max_day+amount, " ist zu hoch oder im Minusbereich")
        else:
            self.Max_day+=amount
            self.Bank_balance+=amount

    def withdraw(self,amount):
        if amount<0 or self.Max_day+amount > self.Max_amount:
            return False
        else:
            self.Bank_balance-=amount
            self.Max_day+=amount
    
account1=Account("Dietmar", 47114812, 14567.37)
print(account1.Max_amount)
value_deposit=eval(input("Wert der Einzahlung: "))
account1.deposit(value_deposit)
print("Der Aktuelle Kontostand von ", account1.Owner, "ist ", round(account1.Bank_balance, 2))
print("Der täglche Umsatz beträgt: ", round(account1.Max_day, 2))

value_withdraw=eval(input("Welchen Betrag möchtest du abheben: "))
account1.withdraw(value_withdraw)
print("Der Aktuelle Kontostand von ", account1.Owner, "ist ", round(account1.Bank_balance, 2))
print("Der täglche Umsatz beträgt: ", round(account1.Max_day, 2))
