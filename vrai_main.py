
import json
from data import *
from tools import *
clients = get_clients_base ()

def ask_for_client_id (message):
    client_id = input (message)
    return client_id

def client_is_valid (client_id):
    print ("Liste des clés : ", list (clients.keys ()))
    return client_id in list (clients.keys ())

def client_is_not_valid (client_id):
    return not (client_is_valid (client_id))

def home_menu():
    client_id = ask_and_validate_client_id ()
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")
    return choice

def run_atm():
    
        while True:
            choice = home_menu()
            if choice == '1':
                check_balance()
            elif choice == '2':
                fonctionnement_depot()
            elif choice == '3':
                retrait()
            elif choice == '4':
                print("Merci. Aurevoir")
                break
            else:
                print("Erreur. Veuillez rentrer à nouveau votre choix (1-4).")
        else:
            print("Erreur. Essayez à nouveau.")