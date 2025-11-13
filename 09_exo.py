while True:
    try:
        user_value = float(input("Entrer un nombre :\n> "))
        break
    except ValueError as e:
        print(f"Vous n'avez pas entré un nombre entier ou flotant.\n>>> {e}\n")

print(f"nombre de l'utilisateur : {user_value}")