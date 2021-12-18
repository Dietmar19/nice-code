"""
author: Dietmar
Date: 18.12.2021
"""

class Mensch:
    def __init__(self, name, length, password):
        self.Name=name
        self.Length=length
        self.Password=password
        

    def checkpassword(self,password):
        if self.Password == password:
            print("Password is correct")
        else:
            print("Passwort is wrong")

mensch1=Mensch("Dietmar", 1.86,"Dagmar38" )
pwd = input("Enter your password:  ")
mensch1.checkpassword(pwd)