def transfert_somme(clients, pseudo):
    print("\n" + "🔁".center(50, "═"))
    print("💸 TRANSFERT D'ARGENT 💸".center(50))
    print("🔁".center(50, "═"))

    destinataire = input("👤 Pseudo du destinataire : ")

    if destinataire not in clients:
        print("❌ Ce destinataire n'existe pas.")
        return

    montant = input("💵 Montant à transférer : ")

    # On vérifie que c'est bien un nombre
    if not montant.replace(".", "", 1).isdigit():
        print("⚠️ Tu dois entrer un nombre.")
        return

    montant = float(montant)

    if montant <= 0:
        print("⚠️ Le montant doit être plus grand que 0.")
        return

    if montant > clients[pseudo]["solde"]:
        print("❌ Tu n'as pas assez d'argent pour faire ce transfert.")
        return

    clients[pseudo]["solde"] -= montant
    clients[destinataire]["solde"] += montant

    print("\n✅ Transfert réussi !")
    print(f"💳 Nouveau solde de {pseudo} : {clients[pseudo]['solde']:.2f} €")
    print(f"💳 Nouveau solde de {destinataire} : {clients[destinataire]['solde']:.2f} €")
    print("✨" * 25 + "\n")
