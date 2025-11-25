def depot_somme(clients, pseudo):
    print("\n" + "💰".center(40, "═"))
    print("💸 DEPÔT D'ARGENT 💸".center(40))
    print("💰".center(40, "═"))

    montant = input("💵 Montant à déposer : ")

    # Vérifie que le montant est bien un nombre
    if not montant.replace(".", "", 1).isdigit():
        print("⚠️ Tu dois entrer un nombre.")
        return

    montant = float(montant)

    if montant <= 0:
        print("⚠️ Le montant doit être plus grand que 0.")
        return

    clients[pseudo]["solde"] += montant

    print("\n✅ Dépôt réussi !")
    print(f"💳 Nouveau solde de {pseudo} : {clients[pseudo]['solde']:.2f} €")
    print("♣" * 20 + "\n")
