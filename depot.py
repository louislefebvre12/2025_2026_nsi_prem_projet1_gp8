def depot_somme(clients, pseudo):
    montant = float(input("Montant à déposer : "))

    if montant <= 0:
        print("Montant invalide.")
        return

    clients[pseudo]["solde"] += montant
    print(f"Dépôt effectué ! Nouveau solde : {clients[pseudo]['solde']} €")