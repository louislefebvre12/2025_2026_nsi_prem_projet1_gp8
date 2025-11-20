
# transfert :

# entrer dans le transfert 
# sélectionner le client à qui envoyer l'argent
# sélectionner le montant à envoyer
# afficher le message de verification de notre action
# retirer la somme du compte du premier client
# ajouter la meme somme au deuxieme client

while client_is_in_transfert_page ():
    show transfert_message
    ask_client1_select_client2 ()
    

    #retrait:
#- choisisser un montant 
#si retrait fait:
#- retirer le montant au solde + noter la date dans un historique

monant = input("Choisissez un montant : ")
message_grosses_coupures : input("Voulez vous des grosses coupures? ")
def message_grosses_coupures() : 
    if 

    #depot:
>>>>>>> Stashed changes
#- rentrer un montant 
#si depot fait: 
#- ajouter le montant au solde + noter la date dans un historique 
import data
from data import *



# reponse_message_depot_verif 

def rep_is_yes (rep):
    return rep in yes_responses

def rep_is_no (rep):
    return not (rep_is_yes (rep)) 

def save_depot_in_historique ():
    pass

def propose_depot ():
    message_depot = "Choisissez un montant "
    montant_depot = input(message_depot) 
    return montant_depot

def add_amount_to_account ():
    pass

def fonctionnement_depot ():
    propose_depot ()
    montant_depot = float(input("Enter the amount to deposit: "))
    print(message_depot_verif) 
    while rep_is_yes :
        if montant_depot > 0:
            add_amount_to_account
            save_depot_in_historique
            print (f"Le montant de {montant_depot}€ a été déposé sur le compte".)
            return return_to_accueil
        else :
            print("Veuillez rentrer un montant positif.")
        return return_to_accueil
    else :
        rep_is_no
        propose_depot
    return return_to_accueil
    






