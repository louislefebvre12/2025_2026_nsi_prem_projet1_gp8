import sys
import os

# Permet d'importer les modules placés dans user_actions
sys.path.append(os.path.join(os.getcwd(), "user_actions"))

from login import login_user
from create_account import register_user
from add_money import deposit_money
from pull_money import withdraw_money
from view_sold import show_balance
from send_money import transfer_money
from settings import account_settings


def main_menu():
    print("MENU PRINCIPAL")
    print("1 - Se connecter")
    print("2 - Créer un compte")
    print("q - Quitter")

    choice = input("Choix : ").strip()

    if choice == "1":
        user = login_user()
    elif choice == "2":
        user = register_user()
        if user is None:
            print("Création annulée ou identifiant déjà utilisé.")
            return
    elif choice.lower() == "q":
        print("Au revoir.")
        return
    else:
        print("Option invalide.")
        return

    user_dashboard(user)


def user_dashboard(user):
    print(f"\nConnexion: {user['name']} (id: {user['id']})\n")

    while True:
        print("ACTIONS")
        print("1 - Voir mon solde")
        print("2 - Retirer de l'argent")
        print("3 - Déposer de l'argent")
        print("4 - Envoyer de l'argent")
        print("5 - Paramètres")
        print("q - Se déconnecter")

        action = input("Action : ").strip()

        if action == "1":
            show_balance(user)

        elif action == "2":
            user = withdraw_money(user) or user

        elif action == "3":
            user = deposit_money(user) or user

        elif action == "4":
            user = transfer_money(user) or user

        elif action == "5":
            should_exit, user = account_settings(user)
            if should_exit:
                print("Compte supprimé. Retour au menu principal.")
                return
            # user may be updated by settings (e.g., name or password change)

        elif action.lower() == "q":
            print("Déconnexion.")
            return

        else:
            print("Option invalide.")


if __name__ == "__main__":
    while True:
        main_menu()
        cont = input("\nRevenir au menu principal ? (o/n) : ").strip().lower()
        if cont != "o":
            print("Fermeture du programme.")
            break


