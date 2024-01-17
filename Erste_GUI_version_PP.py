# Bundesland-Kostenfaktoren Dictionary
bundesland_kostenfaktoren = {
    'Baden-Württemberg': 1.5,
    'Bayern': 1.7,
    'Berlin': 2.1,
    'Brandenburg': 1.1,
    'Bremen': 1.2,
    'Hamburg': 2.5,
    'Hessen': 1.3,
    'Mecklenburg-Vorpommern': 0.9,
    'Niedersachsen': 1,
    'Nordrhein-Westfalen': 1.1,
    'Rheinland-Pfalz': 1,
    'Saarland': 0.7,
    'Sachsen': 0.7,
    'Sachsen-Anhalt': 0.6,
    'Schleswig-Holstein': 1.4,
    'Thüringen': 0.6
}

# Stadt vs. Land Kostenfaktoren Dictionary
stadt_vs_land_kostenfaktoren = {
    'Land': 1,
    'Stadt': 2
}

# Weitere Kostenfaktoren Dictionary
weitere_kostenfaktoren = {
    'QM-Grundstück': {'Preis': 160, 'Einheit': 'pro m²'},
    'QM-Wohnfläche': {'Preis': 2500, 'Einheit': 'pro m²'},
    'Geplant von Architekt': {'Aufschlag': 20, 'Einheit': 'Aufschlag in %'},
    'Makler': {'Aufschlag': 20, 'Einheit': 'Aufschlag in %'},
    'Denkmalschutz': {'Reduzierung': 25, 'Einheit': 'Reduzierung in %'},
    'Baujahr': {'Reduzierung': 0.1, 'Einheit': 'Reduzierung in % pro Jahr'}
}

ausstattung_kostenfaktoren = {
    'Rohbau': 0.5,
    'Sanierungsbedarf': 0.8,
    'Renovierungsbedarf': 0.9,
    'Einfach': 1,
    'Gehoben': 2
}

hausart_kostenfaktoren = {
    'Einfamilienhaus': 1,
    'Doppelhaushälfte': 0.8,
    'Mehrfamilienhaus': 0.7
}


import tkinter as tk
from tkinter import ttk

def calculate_cost():
    grundstuecksflaeche_val = float(grundstuecksflaeche_entry.get())
    wohnflaeche_val = float(wohnflaeche_entry.get())
    architektenhaus_val = architektenhaus_var.get()
    makler_verkauf_val = makler_verkauf_var.get()
    denkmalschutz_val = denkmalschutz_var.get()
    baujahr_val = int(baujahr_entry.get())
    stadt_oder_land_val = stadt_oder_land_var.get()
    ausstattung_val = ausstattung_var.get()
    hausart_val = hausart_var.get()
    bundesland_val = bundesland_var.get()




    print("Grundstücksfläche:", grundstuecksflaeche_val)
    print("Wohnfläche:", wohnflaeche_val)
    print("Architektenhaus:", architektenhaus_val)
    print("Makler Verkauf:", makler_verkauf_val)
    print("Denkmalschutz:", denkmalschutz_val)
    print("Baujahr:", baujahr_val)
    print("Stadt oder Land:", stadt_oder_land_val)
    print("Ausstattung:", ausstattung_val)
    print("Hausart:", hausart_val)
    print("Bundesland:", bundesland_val)


root = tk.Tk()
root.title("Immobilenkostenrechner")
root.geometry("900x500")


background_image = tk.PhotoImage(file="1690897892210.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

style = ttk.Style()
style.configure("TLabel", padding=5, font=('Arial', 12), background=
'rgba(255, 255, 255, 0.7)', foreground='#000080')
style.configure("TButton", padding=5, font=('Arial', 12), background=
'#4169E1', foreground='#FFFFFF')
style.configure("TEntry", padding=5, font=('Arial', 12))
style.configure("TCombobox", padding=5, font=('Arial', 12))

# Grundstücksfläche
grundstuecksflaeche_label = ttk.Label(root, text="Grundstücksfläche (m²):",
                                      style="TLabel")
grundstuecksflaeche_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

grundstuecksflaeche_entry = ttk.Entry(root, style="TEntry")
grundstuecksflaeche_entry.grid(row=0, column=1, padx=10, pady=10)

# Wohnfläche
wohnflaeche_label = ttk.Label(root, text="Wohnfläche (m²):", style="TLabel")
wohnflaeche_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

wohnflaeche_entry = ttk.Entry(root, style="TEntry")
wohnflaeche_entry.grid(row=1, column=1, padx=10, pady=10)

# Architektenhaus
architektenhaus_label = ttk.Label(root, text="Architektenhaus:", style="TLabel")
architektenhaus_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

architektenhaus_var = tk.BooleanVar()
architektenhaus_checkbox = ttk.Checkbutton(root, variable=architektenhaus_var,
                                           style="TCheckbutton")
architektenhaus_checkbox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Makler Verkauf
makler_verkauf_label = ttk.Label(root, text="Makler Verkauf:", style="TLabel")
makler_verkauf_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

makler_verkauf_var = tk.BooleanVar()
makler_verkauf_checkbox = ttk.Checkbutton(root, variable=makler_verkauf_var,
                                          style="TCheckbutton")
makler_verkauf_checkbox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Denkmalschutz
denkmalschutz_label = ttk.Label(root, text="Denkmalschutz:", style="TLabel")
denkmalschutz_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

denkmalschutz_var = tk.BooleanVar()
denkmalschutz_checkbox = ttk.Checkbutton(root, variable=denkmalschutz_var,
                                         style="TCheckbutton")
denkmalschutz_checkbox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Baujahr
baujahr_label = ttk.Label(root, text="Baujahr:", style="TLabel")
baujahr_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

baujahr_entry = ttk.Entry(root, style="TEntry")
baujahr_entry.grid(row=5, column=1, padx=10, pady=10)

# Stadt oder Land
stadt_oder_land_label = ttk.Label(root, text="Stadt oder Land:", style="TLabel")
stadt_oder_land_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

stadt_oder_land_var = tk.StringVar()
stadt_oder_land_combobox = ttk.Combobox(root, textvariable=stadt_oder_land_var,
                                        values=['Stadt', 'Land'], style="TCombobox")
stadt_oder_land_combobox.grid(row=6, column=1, padx=10, pady=10)

# Ausstattung
ausstattung_label = ttk.Label(root, text="Ausstattung:", style="TLabel")
ausstattung_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")

ausstattung_var = tk.StringVar()
ausstattung_combobox = ttk.Combobox(root, textvariable=ausstattung_var, values=
['Rohbau', 'Sanierungsbedarf', 'Renovierungsbedarf', 'Einfach', 'Gehoben'],
                                    style="TCombobox")
ausstattung_combobox.grid(row=7, column=1, padx=10, pady=10)

# Hausart
hausart_label = ttk.Label(root, text="Hausart:", style="TLabel")
hausart_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

hausart_var = tk.StringVar()
hausart_combobox = ttk.Combobox(root, textvariable=hausart_var, values=
['Einfamilienhaus', 'Doppelhaushälfte', 'Mehrfamilienhaus'], style="TCombobox")
hausart_combobox.grid(row=8, column=1, padx=10, pady=10)

# Bundesland
bundesland_label = ttk.Label(root, text="Bundesland:", style="TLabel")
bundesland_label.grid(row=9, column=0, padx=10, pady=10, sticky="w")

bundesland_var = tk.StringVar()
bundesland_combobox = ttk.Combobox(root, textvariable=bundesland_var,
                                   values=list(bundesland_kostenfaktoren.keys
                                               ()), style="TCombobox")
bundesland_combobox.grid(row=9, column=1, padx=10, pady=10)

# Button zum Berechnen
calculate_button = ttk.Button(root, text="Berechnen", command=calculate_cost,
                              style="TButton")
calculate_button.grid(row=10, column=0, columnspan=2, pady=10)


root.mainloop()

