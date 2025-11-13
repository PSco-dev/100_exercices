info_user = {
    "nom"   : "travolta",
    "prenom": "James",
    "age"   : 33,
    "job"   : "plaquiste",
    "marié" : True,
}

for k, v in info_user.items():
    print(f"{k.capitalize()} : {v}")