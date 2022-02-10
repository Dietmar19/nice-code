"""
Author: Dietmar
Date: 09.02.2022
"""
class Account:
    #Max_amount=1500
    def __init__(self, owner, bank_account, bank_balance, max_amount=1500):
        self.Owner=owner
        self.Bank_account=bank_account
        self.Bank_balance=bank_balance    # Kontostand
        self.Max_amount=max_amount
        self.Max_day=0                    #speichert den Wert der bewegten Geldmenge(Ein- und Auszahung)
    def deposit(self, amount):
        if amount < 0 or self.Max_day+amount >self.Max_amount: #
            return print("Einzahlung nicht möglich. Der Betrag: ", self.Max_day+amount, "Euro", " ist zu hoch oder im Minusbereich")
           # return self.Max_amount+amount
        else:
            self.Max_day+=amount
            self.Bank_balance+=amount

    def withdraw(self,amount):
        if amount<0 or self.Max_day+amount > self.Max_amount:
           #return False
           #return self.Max_amount+amount
           return print("Eine Auszahlung ist in dieser Höhe nicht möglich")
        else:
            self.Bank_balance-=amount
            self.Max_day+=amount
    
account1=Account("Dietmar", 47114812, 14567.37)
print("Der maximale Höhe des für den täglichen Geldtransfers sind: ",account1.Max_amount, "Euro")

while True:
    flag = int(input("Geben sie eine 1 ein, wenn sie eine Einzahlung oder eine 2 ein wenn sie eine Auszahlung tätigen wollen:  "))
    if flag == 1:
        value_deposit=eval(input("Welchen Betrag möchtest du einzahlen: "))
        account1.deposit(value_deposit)
        print("Der Aktuelle Kontostand von ", account1.Owner, "ist ", round(account1.Bank_balance, 2))
        print("Der täglche Umsatz beträgt: ", round(account1.Max_day, 2))
    elif flag == 2:
        value_withdraw=eval(input("Welchen Betrag möchtest du abheben: "))
        account1.withdraw(value_withdraw)
        print("Der Aktuelle Kontostand von ", account1.Owner, "ist ", round(account1.Bank_balance, 2))
        print("Der täglche Umsatz beträgt: ", round(account1.Max_day, 2))
    else:
        print("Der eingebene Wert entspricht nur der Vorgabe")
        break
