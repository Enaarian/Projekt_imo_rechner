from kostenfaktoren import (ausstattung_kostenfaktor,
                            bundesland_kostenfaktoren, hausart_kostenfaktor,
                            stadt_vs_land_kostenfaktor, weitere_kostenfaktoren)
def berechne_immobilienpreis(grundstueck, wohnflaeche, architektenhaus,
                             makler, denkmalschutz, baujahr, lage,
                             ausstattung, hausart, bundesland):
    kostenfaktor = bundesland_kostenfaktoren.get(bundesland, 1)

    if lage.lower() in stadt_vs_land_kostenfaktor:
        kostenfaktor *= stadt_vs_land_kostenfaktor[lage.lower()]
    kostenfaktor += grundstueck * (weitere_kostenfaktoren.get("QM-Grundstück",
                                                              0) / 100)
    kostenfaktor += wohnflaeche * (weitere_kostenfaktoren.get("QM-Wohnfläche",
                                                              0) / 100)
    if architektenhaus and "Geplant von Architekt" in weitere_kostenfaktoren:
        kostenfaktor += weitere_kostenfaktoren["Geplant von Architekt"]
    if makler and "Makler" in weitere_kostenfaktoren:
        kostenfaktor += weitere_kostenfaktoren["Makler"]
    if denkmalschutz and "Denkmalschutz" in weitere_kostenfaktoren:
        kostenfaktor += weitere_kostenfaktoren["Denkmalschutz"]
    if "Baujahr" in weitere_kostenfaktoren:
        kostenfaktor += (2022 - baujahr) * weitere_kostenfaktoren["Baujahr"]
    if ausstattung.lower() in ausstattung_kostenfaktor:
        kostenfaktor *= ausstattung_kostenfaktor[ausstattung.lower()]
    if hausart.lower() in hausart_kostenfaktor:
        kostenfaktor *= hausart_kostenfaktor[hausart.lower()]
    return kostenfaktor

# Beispiel Verwendung:
grundstueck = 800
wohnflaeche = 80
architektenhaus = False
makler = True
denkmalschutz = True
baujahr = 1950
lage = 'Land'
ausstattung = 'Einfach'
hausart = 'Einfamilienhaus'
bundesland = 'Baden-Württemberg'

geschaetzter_preis = berechne_immobilienpreis(grundstueck, wohnflaeche,
                                              architektenhaus, makler,
                                              denkmalschutz, baujahr, lage,
                                              ausstattung, hausart, bundesland)
print(f"Geschätzter Preis: {geschaetzter_preis} Euro")