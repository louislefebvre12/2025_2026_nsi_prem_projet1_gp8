#depot:
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
    montant_depot () 

def fonctionnement_depot ():
    propose_depot ()
    print(message_depot_verif) 
    while rep_is_yes :
        add_amount_to_account
        save_depot_in_historique
        return return_to_accueil
    else :
        rep_is_no
        propose_depot
    








fonctionnement_depot ()