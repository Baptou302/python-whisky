"""
MINI-PROJET 01 — LA CALCULATRICE

Le cahier des charges complet est dans le README.md.
Chaque fonction ci-dessous décrit ce qu'elle doit faire dans sa
docstring. Complète-les une par une, dans l'ordre, et lance le
programme après chaque fonction pour tester.

Lancer :  python starter.py
"""


def demander_nombre(message):
    """
    Affiche message, lit la saisie et la renvoie sous forme de float.

    Redemande tant que la saisie n'est pas un nombre valide.
    Pour ça, tente la conversion dans un bloc try, et attrape
    l'erreur ValueError dans un bloc except.
    """
    pass


def demander_operation():
    """
    Demande une opération et la renvoie.

    Seules + - * / sont acceptées : redemande tant que la saisie
    n'en fait pas partie. L'opérateur "in" permet de tester
    l'appartenance à une liste.
    """
    pass


def calculer(a, operation, b):
    """
    Renvoie le résultat de a operation b.

    Renvoie None si l'opération est impossible, c'est-à-dire une
    division par zéro. C'est l'appelant qui décidera quoi afficher.
    """
    pass


def main():
    """
    Boucle principale.

    Répète indéfiniment : demander le premier nombre, l'opération,
    le second nombre, calculer, afficher le résultat ou un message
    d'erreur si le résultat vaut None, puis demander si on continue.
    Sortir de la boucle avec break si la réponse n'est pas "o".
    """
    print("=" * 25)
    print("   CALCULATRICE")
    print("=" * 25)

    print("\nÀ bientôt !")


if __name__ == "__main__":
    main()
