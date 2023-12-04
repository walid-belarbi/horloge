import tkinter as tk
from tkinter import simpledialog, messagebox
from time import strftime, localtime, mktime

def afficher_heure():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)

    # Vérifie si l'alarme est définie et si l'heure actuelle correspond à l'heure de l'alarme
    if alarm_time is not None and strftime('%H:%M:%S') == strftime('%H:%M:%S', localtime(alarm_time)):
        afficher_message_alarme()

    label.after(1000, afficher_heure)  # Met à jour toutes les 1 seconde

def regler_alarme(heure_alarme):
    global alarm_time
    alarm_time = mktime((2000, 1, 1, heure_alarme[0], heure_alarme[1], heure_alarme[2], 0, 0, -1))
    label_alarm.config(text=f'Alarme réglée à {strftime("%H:%M:%S", localtime(alarm_time))}')

def afficher_message_alarme():
    # Affiche un message lorsque l'heure actuelle correspond à l'heure de l'alarme
    messagebox.showinfo("Alarme", "Ding Dong !")

root = tk.Tk()
root.title("Horloge Numérique")

alarm_time = None  # Initialise l'heure de l'alarme à None

label = tk.Label(root, font=('calibri', 40, 'bold',), background='black', foreground='white')
label.pack(anchor='center')

label_alarm = tk.Label(root, font=('calibri', 30), background='black', foreground='white')
label_alarm.pack(anchor='s', pady=10)

# Bouton pour régler l'alarme
button_set_alarm = tk.Button(root, text="Régler l'alarme", command=lambda: regler_alarme(get_heure_alarme()))
button_set_alarm.pack()

def get_heure_alarme():
    # Fonction pour obtenir l'heure de l'alarme sous forme de tuple
    user_input = simpledialog.askstring("Réglage de l'alarme", "Entrez l'heure de l'alarme (HH:MM:SS):")

    # Vérifiez si l'utilisateur a saisi une valeur et si elle est au bon format
    if user_input and len(user_input.split(':')) == 3:
        # Convertissez la saisie de l'utilisateur en tuple d'entiers (heures, minutes, secondes)
        return tuple(map(int, user_input.split(':')))
    else:
        # Affichez un message d'erreur si l'entrée est incorrecte
        messagebox.showerror("Erreur", "Format d'heure incorrect. Réglez à nouveau l'alarme.")
        return None

afficher_heure()

root.mainloop()