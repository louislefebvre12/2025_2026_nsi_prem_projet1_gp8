def voir_solde(clients, pseudo):
    print("\n" + "💳".center(40, "═"))
    print("👁️ SOLDE DU COMPTE 👁️".center(40))
    print("💳".center(40, "═"))

    solde = clients[pseudo]["solde"]
    print(f"💰 Pseudo : {pseudo}")
    print(f"💵 Solde actuel : {solde:.2f} €")
    print("✨" * 20 + "\n")

