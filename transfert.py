
def transfert_somme(clients, pseudo):
    destinataire = input("Pseudo du destinataire : ")

    if destinataire not in clients:
        print("Ce destinataire n'existe pas.")
        return

    montant = float(input("Montant du transfert : "))

    if montant <= 0:
        print("Montant invalide.")
        return

    if montant > clients[pseudo]["solde"]:
        print("Solde insuffisant.")
        return

    clients[pseudo]["solde"] -= montant
    clients[destinataire]["solde"] += montant

    print(f"Transfert réussi ! Nouveau solde : {clients[pseudo]['solde']} €")