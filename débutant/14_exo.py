#!/usr/bin/env python3

def carre(nb):
    return nb * nb

def main():
    user_entry = input("veuillez saisir votre nombre : ")
    try:
        user_entry = float(user_entry)
    except ValueError as e:
        print(f"{e}")
    else:
        print(carre(user_entry))


if __name__ == "__main__":
    main()
