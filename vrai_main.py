
import sys


from login import login_user
from add_money import deposit_money
from pull_money import withdraw_money
from view_sold import show_balance
from send_money import transfer_money
from settings import account_settings
from create_acount import register_user


def main_menu():
    print("=== MENU PRINCIPAL ===")
    print("1 - Se connecter")
    print("2 - Créer un compte")
    print("q - Quitter")

    choix = input("Choix : ").strip()

    if choix == "1":
        user = login_user()
    elif choix == "2":
        user = register_user()
    elif choix == "q":
        print("Au revoir !")
        exit()
    else:
        print("Option invalide.")
        exit()

    user_menu(user)


def user_menu(user):
    print(f"\nConnexion réussie. Bienvenue {user['name']} !\n")

    while True:
        print("=== ACTIONS DISPONIBLES ===")
        print("1 - Voir le solde")
        print("2 - Retirer de l'argent")
        print("3 - Déposer de l'argent")
        print("4 - Envoyer à un autre utilisateur")
        print("5 - Paramètres du compte")
        print("q - Déconnexion")

        action = input("Votre choix : ").strip()

        if action == "1":
            show_balance(user)

        elif action == "2":
            withdraw_money(user)

        elif action == "3":
            deposit_money(user)

        elif action == "4":
            transfer_money(user)

        elif action == "5":
            account_settings(user)

        elif action == "q":
            print("Déconnexion effectuée.")
            exit()

        else:
            print("Choix invalide.")


main_menu()
