import json

clients = { \
    "a.jaouengarcia" : { \
        "pin" : 1234, \
        "solde": 6967, \
        "depots": {  
            "2025-01-01" : 2000, \
            "2025-01-31" : 3020, \
            "2025-05-31" : 2123, \
            "2025-08-01" : 589, \
            "2025-09-01" : 1234
        },
        "retraits": { \
            "2025-01-01" : 2000, \
            "2025-01-31" : 3020, \
            "2025-05-31" : 2123, \
            "2025-08-01" : 589, \
            "2025-09-01" : 1234
        }
    },
    "l.lefebvre": { \
        "pin" : 90210, \
        "solde": 3200, \
        "depots": { \
            "2025-01-01" : 2000, \
            "2025-01-31" : 3020, \
            "2025-05-31" : 2123, \
            "2025-08-01" : 589, \
            "2025-09-01" : 1234
        },
        "retraits": { \
            "2025-01-01" : 2000, \
            "2025-01-31" : 3020, \
            "2025-05-31" : 2123, \
            "2025-08-01" : 589, \
            "2025-09-01" : 1234
        }
    }
}

def load_dico_from_json_file (file_name):
    with open (file_name, "r") as f:
        dico = json.load (f)
    return dico


def save_dico_in_json_file (file_name, dico):
    with open (file_name, "w") as f:
        json.dump (dico, f, indent=4)

save_dico_in_json_file ("toto.json", clients)

dico = load_dico_from_json_file ("toto.json")
print (dico)