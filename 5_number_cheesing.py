
import random
upper_bond= 100
secret_number = random.randint(0,upper_bond)

print("Es wurde eine Zufallszahl zwische 0 und  " + str(upper_bond) + " generiert")
print( "Deine Aufgabe ist es jetzt zu erraten, welche Zahl es ist")
print("Viel Glück")
guess= None
count = 1
while guess != secret_number:
    guess = int(input("Wähle bitte eine Ganzzahl zwischen 0 und 100" + ": "))
    if guess == 0:
        print("Das ist beendet")
        break
    if guess == secret_number:
        print(" ja das ist korrekt")
    elif guess < secret_number:
        print(" Die gesuchte Zahl ist größer als deine geratene Zahl!")
        count+=1
    else:
        print("Die gesuchte Zahl ist kleiner als deine gearatende Zahl!")
        count+=1

print("Du hast " + str(count) + " Versuche benötigt, um die korrekte Zahl zu finden!")

    