"""
CHAPITRE 06 — LES DICTIONNAIRES

EXERCICE 1 — La fiche voiture
    Pars du dictionnaire voiture et effectue ces opérations :
        1. change l'année en 2020
        2. ajoute une clé "couleur" valant "rouge"
        3. supprime la clé "modele"
    Affiche ensuite le dictionnaire, puis chaque clé et sa valeur
    sur une ligne :
        marque : Peugeot
        annee : 2020
        couleur : rouge
    Indice : voiture.items() donne les paires (clé, valeur).

EXERCICE 2 — Le bulletin de la classe
    classe est une LISTE de DICTIONNAIRES.
    Affiche chaque élève avec sa note, puis la moyenne de la classe
    arrondie à 2 décimales, puis uniquement les noms des élèves
    ayant 10 ou plus.
    Attention aux guillemets dans les f-strings : si la f-string est
    en guillemets doubles, utilise des simples à l'intérieur,
    comme {eleve['nom']}.

Lancer :  python exercices.py
"""

print("--- EXERCICE 1 ---")

voiture = {"marque": "Peugeot", "modele": "208", "annee": 2018}


print()
print("--- EXERCICE 2 ---")

classe = [
    {"nom": "Lucas", "note": 12},
    {"nom": "Marie", "note": 17},
    {"nom": "Karim", "note": 8},
    {"nom": "Zoé", "note": 14},
]
