from pathlib import Path

try:
    chemin = Path("../README.md")
    with chemin.open("r") as txt_readme:
        print(txt_readme.read())
except FileNotFoundError as e:
    print(f"erreur, fichier introuvable.\n >>> {e}") 



