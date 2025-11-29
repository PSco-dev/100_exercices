#!/usr/bin/env python3

def verlant(chaine: str) -> str:
    """
    inverse l'ordre d'une chaine de caractère

    Args:
        chaine ( str ): chaine qui sera traitée

    Returns:
        str: Chaine inversé

    """

    return chaine[::-1]

def main():
    user_data = ''
    while not user_data:
        user_data = input("\ndonne moi quelque chose à incerser : \n-> ")
    print("\n\n-> ",verlant(user_data), " <-")

if __name__ == "__main__":
    main()
