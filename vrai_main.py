import json
import os

def charger_clients():
    if not os.path.exists("clients.json") or os.path.getsize("clients.json") == 0:
        print("Fichier clients.json introuvable ou vide → création du fichier par défaut.")
        clients = {
            "jaouengarcia": {"pin": "1234", "solde": 1500},
            "lefebvre": {"pin": "90210", "solde": 800},
            "kaltrachian": {"pin": "9999", "solde": 2500},
            "viala":{"pin": "0000", "solde": 2.5}
        }
        with open("clients.json", "w") as f:
            json.dump(clients, f, indent=4)
        return clients

    with open("clients.json", "r") as f:
        return json.load(f)

def sauvegarder_clients(clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

def connexion(clients):
    print("\n=== Connexion au DAB ===")
    pseudo = input("Entrez votre pseudo : ")
    pin = input("Entrez votre code PIN : ")

    if pseudo in clients and clients[pseudo]["pin"] == pin:
        print("Connexion réussie !\n")
        return pseudo
    else:
        print("Erreur : pseudo ou PIN incorrect.\n")
        return None

def accueil():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Retrait")
    print("2 - Voir le solde")
    print("3 - Dépôt")
    print("4 - Transfert")
    print("5 - Quitter")
    return input("Choisissez une option : ")


