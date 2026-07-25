import json
from datetime import datetime
from pathlib import Path


NOTIZ_DATEI = Path("notizen.json")
ALTE_NOTIZ_DATEI = Path("notizen.txt")


def aktuelle_zeit():
    return datetime.now().strftime("%d.%m.%Y %H:%M")


def notizen_laden():
    if not NOTIZ_DATEI.exists():
        return []

    try:
        inhalt = NOTIZ_DATEI.read_text(encoding="utf-8")
        daten = json.loads(inhalt)

        if isinstance(daten, list):
            return daten

    except (json.JSONDecodeError, OSError):
        print("\nFehler: Die Notizdatei konnte nicht gelesen werden.")

    return []


def notizen_speichern(notizen):
    daten = json.dumps(
        notizen,
        ensure_ascii=False,
        indent=4,
    )

    NOTIZ_DATEI.write_text(daten, encoding="utf-8")


def naechste_id(notizen):
    if not notizen:
        return 1

    return max(notiz["id"] for notiz in notizen) + 1


def alte_notizen_importieren():
    if NOTIZ_DATEI.exists():
        return

    if not ALTE_NOTIZ_DATEI.exists():
        return

    alte_zeilen = ALTE_NOTIZ_DATEI.read_text(
        encoding="utf-8"
    ).splitlines()

    alte_zeilen = [
        zeile.removeprefix("- ").strip()
        for zeile in alte_zeilen
        if zeile.strip()
    ]

    if not alte_zeilen:
        return

    neue_notizen = []

    for nummer, text in enumerate(alte_zeilen, start=1):
        neue_notizen.append(
            {
                "id": nummer,
                "titel": f"Importierte Notiz {nummer}",
                "inhalt": text,
                "erstellt": aktuelle_zeit(),
                "geaendert": aktuelle_zeit(),
            }
        )

    notizen_speichern(neue_notizen)

    sicherung = Path("notizen_alt.txt")
    ALTE_NOTIZ_DATEI.rename(sicherung)

    print("\nAlte Notizen wurden automatisch importiert.")
    print("Sicherung erstellt: notizen_alt.txt")


def notizen_auflisten(notizen):
    if not notizen:
        print("Noch keine Notizen vorhanden.")
        return

    for notiz in notizen:
        print(
            f'{notiz["id"]}. {notiz["titel"]} '
            f'– geändert: {notiz["geaendert"]}'
        )


def notiz_finden(notizen, notiz_id):
    for notiz in notizen:
        if notiz["id"] == notiz_id:
            return notiz

    return None


def notiz_auswaehlen(notizen):
    if not notizen:
        print("\nEs gibt keine Notizen.")
        return None

    print()
    notizen_auflisten(notizen)

    eingabe = input(
        "\nNotiznummer eingeben oder 0 zum Abbrechen: "
    ).strip()

    if eingabe == "0":
        return None

    if not eingabe.isdigit():
        print("\nBitte eine gültige Nummer eingeben.")
        return None

    notiz = notiz_finden(notizen, int(eingabe))

    if not notiz:
        print("\nDiese Notiz existiert nicht.")
        return None

    return notiz


def notiz_anzeigen():
    print("\n=== NOTIZ ANZEIGEN ===")

    notizen = notizen_laden()
    notiz = notiz_auswaehlen(notizen)

    if not notiz:
        return

    print("\n" + "=" * 45)
    print(notiz["titel"])
    print("=" * 45)
    print(f'Erstellt:  {notiz["erstellt"]}')
    print(f'Geändert:  {notiz["geaendert"]}')
    print("-" * 45)
    print(notiz["inhalt"])
    print("=" * 45)


def alle_notizen_anzeigen():
    print("\n=== ALLE NOTIZEN ===\n")

    notizen = notizen_laden()
    notizen_auflisten(notizen)


def notiz_hinzufuegen():
    print("\n=== NEUE NOTIZ ===")

    titel = input("\nTitel: ").strip()

    if not titel:
        print("\nDer Titel darf nicht leer sein.")
        return

    print("\nInhalt der Notiz:")
    inhalt = input("> ").strip()

    if not inhalt:
        print("\nDer Inhalt darf nicht leer sein.")
        return

    notizen = notizen_laden()
    zeit = aktuelle_zeit()

    neue_notiz = {
        "id": naechste_id(notizen),
        "titel": titel,
        "inhalt": inhalt,
        "erstellt": zeit,
        "geaendert": zeit,
    }

    notizen.append(neue_notiz)
    notizen_speichern(notizen)

    print(f'\nNotiz "{titel}" wurde gespeichert.')


def text_anhaengen():
    print("\n=== TEXT AN NOTIZ ANHÄNGEN ===")

    notizen = notizen_laden()
    notiz = notiz_auswaehlen(notizen)

    if not notiz:
        return

    print("\nAktueller Inhalt:")
    print("-" * 45)
    print(notiz["inhalt"])
    print("-" * 45)

    neuer_text = input("\nText anhängen: ").strip()

    if not neuer_text:
        print("\nEs wurde kein Text eingegeben.")
        return

    notiz["inhalt"] += "\n" + neuer_text
    notiz["geaendert"] = aktuelle_zeit()

    notizen_speichern(notizen)

    print("\nDer Text wurde an die Notiz angehängt.")


def titel_aendern():
    print("\n=== TITEL ÄNDERN ===")

    notizen = notizen_laden()
    notiz = notiz_auswaehlen(notizen)

    if not notiz:
        return

    print(f'\nAktueller Titel: {notiz["titel"]}')

    neuer_titel = input("Neuer Titel: ").strip()

    if not neuer_titel:
        print("\nDer Titel wurde nicht geändert.")
        return

    notiz["titel"] = neuer_titel
    notiz["geaendert"] = aktuelle_zeit()

    notizen_speichern(notizen)

    print("\nDer Titel wurde geändert.")


def notiz_loeschen():
    print("\n=== NOTIZ LÖSCHEN ===")

    notizen = notizen_laden()
    notiz = notiz_auswaehlen(notizen)

    if not notiz:
        return

    bestaetigung = input(
        f'\nNotiz "{notiz["titel"]}" wirklich löschen? (j/n): '
    ).strip().lower()

    if bestaetigung != "j":
        print("\nLöschen wurde abgebrochen.")
        return

    notizen.remove(notiz)
    notizen_speichern(notizen)

    print("\nDie Notiz wurde gelöscht.")


def notizen():
    while True:
        print("\n" * 2)
        print("=" * 40)
        print("               NOTIZEN")
        print("=" * 40)
        print()
        print("1. Notizübersicht")
        print("2. Notiz vollständig anzeigen")
        print("3. Neue Notiz erstellen")
        print("4. Text an Notiz anhängen")
        print("5. Titel einer Notiz ändern")
        print("6. Einzelne Notiz löschen")
        print("0. Zurück zum Hauptmenü")
        print()

        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            alle_notizen_anzeigen()
            input("\nENTER drücken...")

        elif auswahl == "2":
            notiz_anzeigen()
            input("\nENTER drücken...")

        elif auswahl == "3":
            notiz_hinzufuegen()
            input("\nENTER drücken...")

        elif auswahl == "4":
            text_anhaengen()
            input("\nENTER drücken...")

        elif auswahl == "5":
            titel_aendern()
            input("\nENTER drücken...")

        elif auswahl == "6":
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


alte_notizen_importieren()


while True:
    print("\n" * 3)
    print("=" * 40)
    print("            PIOS Academy")
    print("=" * 40)
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