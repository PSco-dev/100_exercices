#!/usr/bin/env python3

def Fibonacci(n: int) -> int | list:
    """
    Cette fonction génère la suite de Fibonacci jusqu'a un nombre spécifié 
    de termes.
    
    Args:
        n (int): Le nombre de termes dans la suite de Fibonaccie
    
    Returns:
        list: Une liste contenant la suite de Fibonacci jusqu'a n termes.

    """

    if n <= 1:
        return [n]
    else:
        suite_fibonacci = [0, 1]
        for i in range(2, n):
            prochain_terme = suite_fibonacci[i - 1] + suite_fibonacci[i - 2]
            suite_fibonacci.append(prochain_terme)
        return suite_fibonacci


if __name__ == "__main__":

    # Génrère la suite de Fibonacci jusqu'a 10 termes
    suite_fibonacci = Fibonacci(10)

    # Affiche le resulta 
    print(suite_fibonacci)