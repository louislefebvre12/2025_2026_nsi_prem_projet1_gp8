def transfert_somme(clients, pseudo):
    print("\n" + "🔁".center(50, "═"))
    print("💸 TRANSFERT D'ARGENT 💸".center(50))
    print("🔁".center(50, "═"))

    destinataire = input("👤 Entrez le pseudo du destinataire : ")

    if destinataire not in clients:
        print("❌ Ce destinataire n'existe pas.")
        return

    try:
        montant = float(input("💵 Entrez le montant à transférer : "))
    except ValueError:
        print("⚠️ Montant invalide ! Veuillez entrer un nombre.")
        return

    if montant <= 0:
        print("⚠️ Montant invalide. Le transfert doit être supérieur à 0.")
        return

    if montant > clients[pseudo]["solde"]:
        print("❌ Solde insuffisant pour effectuer ce transfert !")
        return

    clients[pseudo]["solde"] -= montant
    clients[destinataire]["solde"] += montant

    print("\n✅ Transfert effectué avec succès !")
    print(f"💳 Nouveau solde de {pseudo} : {clients[pseudo]['solde']:.2f} €")
    print(f"💳 Nouveau solde de {destinataire} : {clients[destinataire]['solde']:.2f} €")
    print("✨" * 25 + "\n")
