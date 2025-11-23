
import json

from depot import depot_somme
from retrait import retrait_somme
from solde import voir_solde
from transfert import transfert_somme


def charger_clients():
    with open("clients.json", "r") as f:
        return json.load(f)

def sauvegarder_clients(clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

def connexion(clients):
    print("=== Connexion au DAB ===")
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





def main():
    clients = charger_clients()

    utilisateur = None
    while utilisateur is None:
        utilisateur = connexion(clients)

    while True:
        choix = accueil()

        if choix == "1":
            retrait(clients, utilisateur)
        elif choix == "2":
            voir_solde(clients, utilisateur)
        elif choix == "3":
            depot(clients, utilisateur)
        elif choix == "4":
            transfert(clients, utilisateur)
        elif choix == "5":
            sauvegarder_clients(clients)
            print("Merci d'avoir utilisé le DAB.")
            break
        else:
            print("Option invalide.")

        sauvegarder_clients(clients)

main()
