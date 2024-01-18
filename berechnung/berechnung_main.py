from berechnung.kostenfaktoren import (ausstattung_kostenfaktor,
                            bundesland_kostenfaktoren, hausart_kostenfaktor,
                            stadt_vs_land_kostenfaktor, weitere_kostenfaktoren)
def berechne_immobilienpreis(grundstueck, wohnflaeche, architektenhaus,
                             makler, denkmalschutz, baujahr, lage,
                             ausstattung, hausart, bundesland):
    kostenfaktor = bundesland_kostenfaktoren.get(bundesland, 1)

    if lage.lower() in stadt_vs_land_kostenfaktor:
        kostenfaktor *= stadt_vs_land_kostenfaktor[lage.lower()]
    kostenfaktor += grundstueck * (weitere_kostenfaktoren.get("QM-Grundstück",
                                                              0))
    kostenfaktor += wohnflaeche * (weitere_kostenfaktoren.get("QM-Wohnfläche",
                                                              0))
    if architektenhaus and "Geplant von Architekt" in weitere_kostenfaktoren:
        kostenfaktor *= (weitere_kostenfaktoren["Geplant von Architekt"]/100+1)
    if makler and "Makler" in weitere_kostenfaktoren:
        kostenfaktor *= (weitere_kostenfaktoren["Makler"]/100+1)
    if denkmalschutz and "Denkmalschutz" in weitere_kostenfaktoren:
        kostenfaktor *= (1-weitere_kostenfaktoren["Denkmalschutz"]/100*-1)
    if "Baujahr" in weitere_kostenfaktoren:
        kostenfaktor *= (1+(2024 - baujahr) * (weitere_kostenfaktoren[
            "Baujahr"]/100*-1))
    if ausstattung.lower() in ausstattung_kostenfaktor:
        kostenfaktor *= ausstattung_kostenfaktor[ausstattung.lower()]
    if hausart.lower() in hausart_kostenfaktor:
        kostenfaktor *= hausart_kostenfaktor[hausart.lower()]
    return kostenfaktor

# grundstueck = 800
# wohnflaeche = 80
# architektenhaus = True
# makler = True
# denkmalschutz = True
# baujahr = 1950
# lage = 'Land'
# ausstattung = 'Einfach'
# hausart = 'Einfamilienhaus'
# bundesland = 'Baden-Württemberg'
#
# geschaetzter_preis = berechne_immobilienpreis(grundstueck, wohnflaeche,
#                                               architektenhaus, makler,
#                                               denkmalschutz, baujahr, lage,
#                                               ausstattung, hausart, bundesland)
# print(f"Geschätzter Preis: {geschaetzter_preis:.2f} Euro")