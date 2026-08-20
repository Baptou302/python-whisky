"""
CHAPITRE 07 — LES CHAÎNES DE CARACTÈRES

EXERCICE 1 — Nettoyer et découper
    La variable ligne contient une saisie mal formatée.
    Nettoie-la et découpe-la pour récupérer le prénom, l'âge et la
    ville dans trois variables, puis affiche exactement :
        "Lucas a 25 ans et habite à Lyon"
    Le prénom doit avoir une majuscule et le reste en minuscules.
    Indices : .strip() enlève les espaces autour, .split(",") découpe
    sur les virgules, .capitalize() met la première lettre en majuscule.

EXERCICE 2 — Le palindrome
    Un palindrome se lit pareil dans les deux sens : kayak, radar, ressasser.
    Complète la fonction est_palindrome pour qu'elle renvoie True ou False,
    en ignorant les majuscules.
    Indice : mot[::-1] renvoie le mot à l'envers.

Lancer :  python exercices.py
"""

print("--- EXERCICE 1 ---")

ligne = "   lUcAs,25,Lyon   "


print()
print("--- EXERCICE 2 ---")


def est_palindrome(mot):
    """Renvoie True si le mot se lit pareil dans les deux sens."""
    pass


print(est_palindrome("kayak"))
print(est_palindrome("Radar"))
print(est_palindrome("python"))
