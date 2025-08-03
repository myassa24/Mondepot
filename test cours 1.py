import tkinter as tk

class CesarApp:
    def __init__(self):
        self.fenetre_principale = tk.Tk()
        self.fenetre_principale.title("Chiffrement César")
        self.fenetre_principale.geometry("650x450")
        self.fenetre_principale.configure(bg="cadetblue")

        # Widgets avec noms d'origine
        global label1, label2, text_zone1, text_zone2, label3, label4

        label1 = tk.Label(self.fenetre_principale, text="Texte", bg="linen", font=("Arial", 14, "bold"), fg="black")
        label1.pack(pady=20)

        text_zone1 = tk.Entry(self.fenetre_principale, width=40)
        text_zone1.pack()

        label2 = tk.Label(self.fenetre_principale, text="Clé (décalage)", bg="linen", font=("Arial", 14, "bold"), fg="black")
        label2.pack(pady=12)

        text_zone2 = tk.Entry(self.fenetre_principale, width=10)
        text_zone2.pack()

        bouton_1 = tk.Button(self.fenetre_principale, text="Chiffrer", width=7, font=("Arial", 14, "bold"), command=self.on_chiffrer)
        bouton_1.pack(pady=11)
