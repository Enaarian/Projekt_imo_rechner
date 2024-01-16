# Import (Kostenfaktoren aus den separaten py.datein)
from bundesland_kostenfaktor import bundesland_kostenfaktoren
from stadt_vs_land_kostenfaktor import stadt_vs_land_kostenfaktor
from ausstattung_kostenfaktor import ausstattung_kostenfaktor
from hausart_kostenfaktor import hausart_kostenfaktor
from weitere_kostenfaktoren import weitere_kostenfaktoren

# Benutzereingaben
grundstueck_m2 = float(input("Wie viel m² Grundstück? "))
wohnflaeche_m2 = float(input("Wie viel m² Wohnfläche? "))
architektenhaus = input("Handelt es sich um ein Architektenhaus? (Ja/Nein) ").lower() == "ja"
makler_verkauf = input("Soll ein Makler das Haus verkaufen? (Ja/Nein) ").lower() == "ja"
denkmalschutz = input("Steht das Haus oder Teile davon unter Denkmalschutz? (Ja/Nein) ").lower() == "ja"
baujahr = int(input("Welches Baujahr hat das Haus? "))
stadt_oder_land = input("Ist das Haus in der Stadt oder auf dem Land? (Stadt/Land) ")
ausstattung = input("Wie ist die Ausstattung? (Rohbau/Sanierungsbedarf/Renovierungsbedarf/Einfach/Gehoben) ")
hausart = input("Wie ist die Hausart? (Einfamilienhaus/Doppelhaushälfte/Mehrfamilienhaus) ")
bundesland = input("In welchem Bundesland steht das Haus? ")


# Kostenfaktoren berechnungen
kostenfaktor = 1

kostenfaktor *= bundesland_kostenfaktoren.get(bundesland, 1)
kostenfaktor *= stadt_vs_land_kostenfaktor.get(stadt_oder_land, 1)
kostenfaktor *= ausstattung_kostenfaktor.get(ausstattung, 1)
kostenfaktor *= hausart_kostenfaktor.get(hausart, 1)

if architektenhaus:
    kostenfaktor += weitere_kostenfaktoren["Geplant von Architekt"]

if makler_verkauf:
    kostenfaktor += weitere_kostenfaktoren["Makler"]

if denkmalschutz:
    kostenfaktor += weitere_kostenfaktoren["Denkmalschutz"]

kostenfaktor += (baujahr - 2024) * weitere_kostenfaktoren["Baujahr"]            # hypo. Aktuelles Jahr ist 2024

preis_grundstueck = grundstueck_m2 * weitere_kostenfaktoren["QM-Grundstück"]    # Berechnung des Preises
preis_wohnflaeche = wohnflaeche_m2 * weitere_kostenfaktoren["QM-Wohnfläche"]

gesamtpreis = (preis_grundstueck + preis_wohnflaeche) * kostenfaktor

print(f"Der Gesamtpreis für die Immobilie beträgt {gesamtpreis} Euro.")         # Ausgabe des Ergebnisses
