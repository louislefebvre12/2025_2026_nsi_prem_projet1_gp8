BOGDAN KALTRACHIAN
AXEL VIALA
ALEXANDRE JAOUEN GARCIA
LOUIS LEFEBVRE

# 2025_2026_nsi_prem_projet1_gp8


Ce projet simule un DAB (Distributeur Automatique de Billets) en Python.  
Il permet à un utilisateur de se connecter avec un pseudo et un code PIN, pour effectuer les différentes actions suivantes :

✔️ Retrait  
✔️ Dépôt  
✔️ Consultation du solde  
✔️ Transfert d’argent vers un autre utilisateur  

Le système fait automatiquement la mise à jour du fichier JSON des comptes.


# 📁 Structure du projet

## 🧑‍💻 Fonctionnalités

### 🔐 Connexion
L’utilisateur doit entrer :
- un pseudo
- un code PIN

La connexion est assuré avec la vérification du fichier "clients.json".  
Avec tout le respect l'affichage est plutot mal avec les emojis et les bordures dans le système.

### 🏠 Menu principal
Après la connexion, l’utilisateur accède au menu d'accueil proposant les différentes actions possibles:

1. 💸 Retrait  
2. 👁️ Voir le solde  
3. ➕ Dépôt  
4. 🔁 Transfert vers un autre utilisateur  
5. 🚪 Quitter  

### 💳 Retrait
Permet de retirer de l’argent si le solde du compte connecté est suffisant.  
Affichage avec des emojis et des messages clairs et concis.

### 💰 Dépôt
Ajoute un montant au solde du compte connecté.  
Affichage avec des emojis et des messages clairs et concis.

### 👁️ Solde
Affiche le solde actuel de l’utilisateur connecté avec pseudo et montant formaté.

### 🔄 Transfert
Permet d’envoyer de l’argent à un autre utilisateur présent dans le fichier "clients.json".  
Affichage des soldes mis à jour pour les deux comptes l'envoyeur et le receveur.

### 💾 Sauvegarde automatique
Chaque opération met à jour "clients.json" :

- les soldes restent persistants  
- aucune base de données externe nécessaire  

## 📦 Exécution

### Exécution du programme
python dab.py

### 📁 Exemple de fichier JSON
{
    "jaouengarcia": {
        "pin": "1234",
        "solde": 1500
    },
    "lefebvre": {
        "pin": "90210",
        "solde": 800
    },
    "kaltrachian": {
        "pin": "9999",
        "solde": 2500
    },
    "viala": {
        "pin": "0000",
        "solde": 2500
    }
}

