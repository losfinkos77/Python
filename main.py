def notizen():
    print()
    print("=== NOTIZEN ===")
    print("Hier entstehen später deine Notizen.")


def passwortgenerator():
    print()
    print("=== PASSWORTGENERATOR ===")
    print("Hier entsteht später der Passwortgenerator.")


def rechner():
    print()
    print("=== RECHNER ===")
    print("Hier entsteht später der Rechner.")


print("=" * 30)
print("     PIOS Academy")
print("=" * 30)

print()
print("1. Notizen")
print("2. Passwortgenerator")
print("3. Rechner")
print("0. Beenden")

print()

auswahl = input("Bitte wähle einen Menüpunkt: ")

if auswahl == "1":
    notizen()

elif auswahl == "2":
    passwortgenerator()

elif auswahl == "3":
    rechner()

elif auswahl == "0":
    print("Programm wird beendet.")

else:
    print("Ungültige Eingabe.")