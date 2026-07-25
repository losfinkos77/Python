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

print()

if auswahl == "1":
    print("Notizen werden geöffnet...")

elif auswahl == "2":
    print("Passwortgenerator wird geöffnet...")

elif auswahl == "3":
    print("Rechner wird geöffnet...")

elif auswahl == "0":
    print("Programm wird beendet.")

else:
    print("Ungültige Eingabe!")