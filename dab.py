
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
    print("\n" + "🔐".center(50, "═"))
    print("🔑 CONNEXION AU DAB 🔑".center(50))
    print("🔐".center(50, "═"))

    pseudo = input("👤 Entrez votre pseudo : ")
    pin = input("🔢 Entrez votre code PIN : ")

    if pseudo in clients and clients[pseudo]["pin"] == pin:
        print("\n✅ Connexion réussie ! Bienvenue,", pseudo)
        print("♥" * 50 + "\n")
        return pseudo
    else:
        print("\n❌ Erreur : pseudo ou PIN incorrect.\n")
        return None


def accueil():
    print("\n" + "🏦".center(69, "═"))
    print("💸 DISTRIBUTEUR AUTOMATIQUE DE BILLETS (ALEX, LOUIS, AXEL, BOGDAN) 💸".center(50))
    print("🏦".center(68, "═"))
    print("1️⃣  Retrait")
    print("2️⃣  Voir le solde")
    print("3️⃣  Dépôt")
    print("4️⃣  Transfert")
    print("5️⃣  Quitter")
    print("♥" * 50)
    
    choix = input("➡️  Choisissez une option : ")
    return choix






def main():
    clients = charger_clients()

    utilisateur = None
    while utilisateur is None:
        utilisateur = connexion(clients)

    while True:
        choix = accueil()

        if choix == "1":
            retrait_somme(clients, utilisateur)
        elif choix == "2":
            voir_solde(clients, utilisateur)
        elif choix == "3":
            depot_somme(clients, utilisateur)
        elif choix == "4":
            transfert_somme(clients, utilisateur)
        elif choix == "5":
            sauvegarder_clients(clients)
            print("Merci d'avoir utilisé le DAB.")
            break
        else:
            print("Option invalide.")

        sauvegarder_clients(clients)

main()
