from pathlib import Path


NOTIZ_DATEI = Path("notizen.txt")


def notizen_laden():
    if not NOTIZ_DATEI.exists():
        return []

    zeilen = NOTIZ_DATEI.read_text(encoding="utf-8").splitlines()

    notizen = []

    for zeile in zeilen:
        zeile = zeile.strip()

        if zeile.startswith("- "):
            zeile = zeile[2:]

        if zeile:
            notizen.append(zeile)

    return notizen


def notizen_speichern(notizen):
    with NOTIZ_DATEI.open("w", encoding="utf-8") as datei:
        for notiz in notizen:
            datei.write(f"- {notiz}\n")


def notizen_anzeigen():
    print("\n=== GESPEICHERTE NOTIZEN ===\n")

    notizen = notizen_laden()

    if not notizen:
        print("Noch keine Notizen vorhanden.")
        return

    for nummer, notiz in enumerate(notizen, start=1):
        print(f"{nummer}. {notiz}")


def notiz_hinzufuegen():
    print("\n=== NEUE NOTIZ ===")

    text = input("\nNotiz eingeben: ").strip()

    if not text:
        print("\nKeine Notiz eingegeben.")
        return

    notizen = notizen_laden()
    notizen.append(text)
    notizen_speichern(notizen)

    print("\nNotiz wurde gespeichert.")


def notiz_loeschen():
    print("\n=== NOTIZ LÖSCHEN ===\n")

    notizen = notizen_laden()

    if not notizen:
        print("Es gibt keine Notizen.")
        return

    for nummer, notiz in enumerate(notizen, start=1):
        print(f"{nummer}. {notiz}")

    print()
    eingabe = input(
        "Nummer der zu löschenden Notiz eingeben "
        "oder 0 zum Abbrechen: "
    ).strip()

    if eingabe == "0":
        print("\nLöschen wurde abgebrochen.")
        return

    if not eingabe.isdigit():
        print("\nBitte eine gültige Nummer eingeben.")
        return

    nummer = int(eingabe)

    if nummer < 1 or nummer > len(notizen):
        print("\nDiese Notiznummer existiert nicht.")
        return

    ausgewaehlte_notiz = notizen[nummer - 1]

    bestaetigung = input(
        f'\nNotiz "{ausgewaehlte_notiz}" wirklich löschen? (j/n): '
    ).strip().lower()

    if bestaetigung != "j":
        print("\nLöschen wurde abgebrochen.")
        return

    geloeschte_notiz = notizen.pop(nummer - 1)
    notizen_speichern(notizen)

    print(f'\nNotiz "{geloeschte_notiz}" wurde gelöscht.')


def notizen():
    while True:
        print("\n" * 2)
        print("=" * 35)
        print("            NOTIZEN")
        print("=" * 35)
        print()
        print("1. Notizen anzeigen")
        print("2. Neue Notiz hinzufügen")
        print("3. Einzelne Notiz löschen")
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
            notiz_loeschen()
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