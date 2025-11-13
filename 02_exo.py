saisi_user = input("entrer un nombre : ")
try:
    saisi_user = int(saisi_user)
except ValueError as e:
    print("entrer un nombre entier.\n-> ", e)
    exit()

if saisi_user > 0:
    message = "positif !"
elif saisi_user < 0:
    message = "négatif !"
else:
    message = "c'est zero !"

print(message)