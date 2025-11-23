def depot_somme(clients, pseudo):
    print("\n" + "💰".center(40, "═"))
    print("💸 DEPÔT D'ARGENT 💸".center(40))
    print("💰".center(40, "═"))

    try:
        montant = float(input("💵 Entrez le montant à déposer : "))
    except ValueError:
        print("⚠️  Montant invalide ! Veuillez entrer un nombre.")
        return

    if montant <= 0:
        print("⚠️  Montant invalide. Le dépôt doit être supérieur à 0.")
        return

    clients[pseudo]["solde"] += montant

    print("\n✅ Dépôt effectué avec succès !")
    print(f"💳 Nouveau solde de {pseudo} : {clients[pseudo]['solde']:.2f} €")
    print("✨" * 20 + "\n")
