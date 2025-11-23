def retrait_somme(clients, pseudo):
    montant = float(input("Montant à retirer : "))

    if montant <= 0:
        print("Montant invalide.")
        return

    if montant > clients[pseudo]["solde"]:
        print("Solde insuffisant.")
    else:
        clients[pseudo]["solde"] -= montant
        print(f"Retrait effectué ! Nouveau solde : {clients[pseudo]['solde']} €")