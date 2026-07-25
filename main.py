def notizen():
    print()
    print("=== NOTIZEN ===")
    print("Hier entstehen später deine Notizen.")
    input("\nENTER drücken...")


def passwortgenerator():
    print()
    print("=== PASSWORTGENERATOR ===")
    print("Hier entsteht später der Passwortgenerator.")
    input("\nENTER drücken...")


def rechner():
    print()
    print("=== RECHNER ===")
    print("Hier entsteht später der Rechner.")
    input("\nENTER drücken...")


while True:

    print("\n" * 3)
    print("=" * 35)
    print("         PIOS Academy")
    print("=" * 35)

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
        print("\nProgramm wird beendet.")
        break

    else:
        print("\nUngültige Eingabe.")
        input("ENTER drücken...")