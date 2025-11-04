
#mesaages automatiques

yes_responses = ["oui", "Oui", "O"]
quitting_words = ["ciao","bye","aurevoir","salut","quit","end"]
nombre_pour_faire_action = [1,2,3,4,5,6] # 1=solde 2=historique 3=dépot 4=retrait 5=transfert 6=quitter le meilleur ATM

message_goodbye = "Merci de votre confiance à bientot"
message_bienvenue = "Bonjour ou bonsoir cela dépend de l'heure qu'il est chez vous bienvenue sur votre ATM préféré ;)"

message_to_ask_client_id = "Merci de bien vouloir rentrer votre numéro client : "
message_to_ask_again_client_id = "Merci de BIEN vouloir saisir votre numéro client correcte cette fois-ci : "
message_to_ask_what_action_to_do = "Choisissez une action parmis les 6 :"
message_to_ask_again_what_action_to_do = "Choisissez une action seulement parmis les 6 (PS. : Relire le Read.me)"




def return_to_accueil ():
    pass

import datetime

save_depot_in_historique = datetime.datetime.now()
print(save_depot_in_historique) 

save_withdraw_in_historique = datetime.datetime.now()
print(save_withdraw_in_historique) 

save_transfert_in_historique = datetime.datetime.now()
print(save_transfert_in_historique) 








#Pour depot:

message_depot_verif = f"Etes-vous sur de vouloir déposer cette somme: {montant_depot}€ ? "




#clients

client_001_id = 001 : { "nom" : "Kaltrachian"/
                      "prenom" : "Bogdan" /
                      "solde" : "346" / 
                      "historique_depot" : "[206,"save_depot_in_historique"]" /
                      "historique_retrait" :"[20,"save_withdraw_in_historique"]" /
                      "historique_transfert" : "[34,id_client_recepteur,"save_transfert_in_historique"]"}

client_001_id = 002 : { "nom" : "Viara"/
                      "prenom" : "Axel" /
                      "solde" : "3" / 
                      "historique_depot" : "[4,"save_depot_in_historique"]" /
                      "historique_retrait" :"[10,"save_withdraw_in_historique"]" /
                      "historique_transfert" : "[2200,id_client_recepteur,"save_transfert_in_historique"]"}

client_001_id = 003 : { "nom" : "Jaouen Garcia"/
                      "prenom" : "Alexandre" /
                      "solde" : "67000" / 
                      "historique_depot" : "[267,"save_depot_in_historique"]" /
                      "historique_retrait" :"[70,"save_withdraw_in_historique"]" /
                      "historique_transfert" : "[567,id_client_recepteur,"save_transfert_in_historique"]"}

client_001_id = 004 : { "nom" : "Lefebvre"/
                      "prenom" : "Louis" /
                      "solde" : "90210" / 
                      "historique_depot" : "[3500,"save_depot_in_historique"]" /
                      "historique_retrait" :"[60,"save_withdraw_in_historique"]" /
                      "historique_transfert" : "[12,id_client_recepteur,"save_transfert_in_historique"]"}