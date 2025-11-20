

    #retrait:
#- choisisser un montant 
#si retrait fait:
#- retirer le montant au solde + noter la date dans un historique

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
    print(f"Etes-vous sur de déposer {montant_depot}€ dans votre compte ?") 
    while rep_is_yes :
        if montant_depot > 0:
            add_amount_to_account
            save_depot_in_historique
            print (f"Le montant de {montant_depot}€ a été déposé sur le compte.")
            return return_to_accueil
        else :
            print("Veuillez rentrer un montant positif.")
        return return_to_accueil
    else :
        rep_is_no
        propose_depot
    return return_to_accueil
    

# entrer dans le transfert 
# sélectionner le client à qui envoyer l'argent
# sélectionner le montant à envoyer
# afficher le message de verification de notre action
# retirer la somme du compte du premier client
# ajouter la meme somme au deuxieme client
# noter la date du transfert et les détails dans l'historique


transfert_message_welcome = "Bienvenue dans votre page de transfert !"
message_to_ask_the_amount_for_a_transfert = "Veuillez saisir le montant à transférer : "
message_to_reask_the_amount_for_a_transfert = "Veuillez ressaisir s'il vous plaît le montant à transférer : "
message_to_ask_the_amount_for_a_withdrawal = "Veuillez saisir le montant à retirer : "
message_to_reask_the_amount_for_a_withdrawal = "Veuillez ressaisir s'il vous plaît le montant à retirer : "

code_secret = "1234"
solde_compte = 750.0
solde_destinataire = 150.0


def authentification():
    #Vérifie le code PIN de l'utilisateur.
    essais = 3
    while essais > 0:
        code = input("Veuillez entrer le code PIN de votre compte bancaire: ")
        if code == code_secret:
            print("✔️ Authentification réussie.\n")
            return True
        else:
            essais -= 1
            print("❌ Code incorrect. Il vous reste", essais, "essai(s).\n")
    print("⛔ Votre carte bancaire est bloquée.")
    return False


def transfert(solde, solde_dest):
    "Effectue un transfert d'un compte à un autre."
    print("Bienvenue dans votre page de Transfert")
    print(f"Votre solde est de  {solde} €")

    try:
        montant = float(input("Le montant à transférer : "))
    except ValueError:
        print("❌ Le montant est invalide.")
        return solde, solde_dest

    if montant <= 0:
        print("❌ Le montant doit être strictement positif.")
    elif montant > solde:
        print("❌ Vous n'avez pas assez d'argent sur votre compte bancaire pour effectuer ce transfert.")
    else:
        solde -= montant
        solde_dest += montant
        print(f"✔️ Le transfert de {montant} € a été effectué avec succès !")
        print(f"Votre nouveau solde est de {solde} €")
        print(f"Le solde du destinataire est de {solde_dest} €")

    return solde, solde_dest


print("Vérification du code PIN secret de l'utilisateur...")
if authentification():
    solde_compte, solde_destinataire = transfert(solde_compte, solde_destinataire)
   





