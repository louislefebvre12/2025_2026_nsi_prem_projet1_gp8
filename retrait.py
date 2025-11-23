def retrait_somme(clients, pseudo):
    print("\n" + "💸".center(40, "═"))
    print("💰 RETRAIT D'ARGENT 💰".center(40))
    print("💸".center(40, "═"))

    montant = input("💵 Montant à retirer : ")

    # On vérifie que le montant est bien un nombre
    if not montant.replace(".", "", 1).isdigit():
        print("⚠️ Tu dois entrer un nombre.")
        return

    montant = float(montant)

    if montant <= 0:
        print("⚠️ Le montant doit être plus grand que 0.")
        return

    if montant > clients[pseudo]["solde"]:
        print("❌ Tu n'as pas assez d'argent.")
        return

    clients[pseudo]["solde"] -= montant

    print("\n✅ Retrait réussi !")
    print(f"💳 Nouveau solde : {clients[pseudo]['solde']:.2f} €")
    print("✨" * 20 + "\n")
