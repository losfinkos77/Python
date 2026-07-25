from pathlib import Path


NOTIZ_DATEI = Path("notizen.txt")


def notizen_anzeigen():
    print("\n=== GESPEICHERTE NOTIZEN ===\n")

    if not NOTIZ_DATEI.exists():
        print("Noch keine Notizen vorhanden.")
        return

    inhalt = NOTIZ_DATEI.read_text(encoding="utf-8").strip()

    if not inhalt:
        print("Noch keine Notizen vorhanden.")
        return

    print(inhalt)


def notiz_hinzufuegen():
    print("\n=== NEUE NOTIZ ===")

    text = input("\nNotiz eingeben: ").strip()

    if not text:
        print("\nKeine Notiz eingegeben.")
        return

    with NOTIZ_DATEI.open("a", encoding="utf-8") as datei:
        datei.write(f"- {text}\n")

    print("\nNotiz wurde gespeichert.")


def notizen_loeschen():
    print("\n=== NOTIZEN LÖSCHEN ===")

    if not NOTIZ_DATEI.exists():
        print("\nEs gibt keine Notizen.")
        return

    bestaetigung = input(
        "\nWirklich alle Notizen löschen? (j/n): "
    ).strip().lower()

    if bestaetigung == "j":
        NOTIZ_DATEI.write_text("", encoding="utf-8")
        print("\nAlle Notizen wurden gelöscht.")
    else:
        print("\nLöschen wurde abgebrochen.")


def notizen():
    while True:
        print("\n" * 2)
        print("=" * 35)
        print("            NOTIZEN")
        print("=" * 35)
        print()
        print("1. Notizen anzeigen")
        print("2. Neue Notiz hinzufügen")
        print("3. Alle Notizen löschen")
        print("0. Zurück zum Hauptmenü")
        print()

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            notizen_anzeigen()
            input("\nENTER drücken...")

        elif auswahl == "2":
            notiz_hinzufuegen()
            input("\nENTER drücken...")

        elif auswahl == "3":
            notizen_loeschen()
            input("\nENTER drücken...")

        elif auswahl == "0":
            return

        else:
            print("\nUngültige Eingabe.")
            input("ENTER drücken...")


def passwortgenerator():
    print("\n=== PASSWORTGENERATOR ===")
    print("Hier entsteht später der Passwortgenerator.")
    input("\nENTER drücken...")


def rechner():
    print("\n=== RECHNER ===")
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

    auswahl = input("Bitte wähle einen Menüpunkt: ").strip()

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
    