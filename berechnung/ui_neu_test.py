import tkinter
import tkinter.messagebox
import customtkinter
from berechnung.kostenfaktoren import (ausstattung_kostenfaktor,
                                       bundesland_kostenfaktoren,
                                       hausart_kostenfaktor,
                                       stadt_vs_land_kostenfaktor,
                                       weitere_kostenfaktoren)


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
        kostenfaktor /= (1+(baujahr - 2024) * (weitere_kostenfaktoren[
            "Baujahr"]/100))

    if ausstattung in ausstattung_kostenfaktor:
        kostenfaktor *= ausstattung_kostenfaktor[ausstattung]

    if hausart in hausart_kostenfaktor:
        kostenfaktor *= hausart_kostenfaktor[hausart]

    if bundesland in bundesland_kostenfaktoren:
        kostenfaktor *= bundesland_kostenfaktoren[bundesland]

    if lage in stadt_vs_land_kostenfaktor:
        kostenfaktor *= stadt_vs_land_kostenfaktor[lage]

    return kostenfaktor


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Berechne Immobilienpreis", command=self.berechne_preis_event)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # ... (weitere GUI-Elemente bleiben unverändert)

    def berechne_preis_event(self):
        try:
            # Hier rufe die Funktion berechne_immobilienpreis mit den entsprechenden Parametern auf.
            # Beachte, dass du die Parameterwerte aus den GUI-Elementen wie Entry oder OptionMenu bekommen musst.

            # Beispiel:
            grundstueck = float(self.entry.get())  # Annahme: Grundstücksgröße wird als Zahl eingegeben
            wohnflaeche = 150  # Hier musst du den Wert aus dem GUI erhalten
            architektenhaus = False  # Hier musst du den Wert aus dem GUI erhalten (z.B., Checkbox-Status)
            # ... (andere Parameter entsprechend)

            # Rufe die Funktion auf
            immobilienpreis = berechne_immobilienpreis(grundstueck, wohnflaeche, architektenhaus,
                                                       # ... (andere Parameter entsprechend))

            # Zeige das Ergebnis an (z.B., mit einem MessageBox)
            tkinter.messagebox.showinfo("Ergebnis", f"Der berechnete Immobilienpreis beträgt: {immobilienpreis}")

        except ValueError:
            tkinter.messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl für das Grundstück ein.")

    # ... (weitere Event-Handler bleiben unverändert)


if __name__ == "__main__":
    app = App()
    app.mainloop()