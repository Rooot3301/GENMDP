import tkinter as tk
import string
import random

def generate_password():
    # Génère un mot de passe aléatoire de la longueur spécifiée
    # en utilisant les lettres et les chiffres
    password_characters = string.ascii_letters + string.digits
    length = int(length_entry.get())
    password = ''.join(random.choice(password_characters) for i in range(length))
    password_label.config(text=password)

# Crée la fenêtre principale
window = tk.Tk()
window.title("Générateur de mot de passe")

# Crée un label pour demander à l'utilisateur combien de caractères il souhaite pour son mot de passe
length_label = tk.Label(text="Combien de caractères souhaitez-vous pour votre mot de passe ?")
length_label.pack()

# Crée une entrée pour la longueur du mot de passe
length_entry = tk.Entry()
length_entry.pack()

# Crée un bouton pour générer le mot de passe
generate_button = tk.Button(text="Générer", command=generate_password)
generate_button.pack()

# Crée un label pour afficher le mot de passe
password_label = tk.Label(text="")
password_label.pack()

# Affiche la fenêtre
window.mainloop()

