"""
CHAPITRE 05 — LES LISTES

EXERCICE 1 — La liste de courses
    Pars de la liste courses et effectue ces opérations dans l'ordre :
        1. ajoute "beurre" à la fin
        2. supprime "lait"
        3. insère "café" en première position
    Affiche ensuite la liste, puis chaque article numéroté :
        1. café
        2. pain
        3. oeufs
        4. beurre
    Indice : enumerate(courses) donne l'index ET la valeur.

EXERCICE 2 — Les statistiques
    À partir de la liste notes :
        - affiche le nombre de notes, la plus basse et la plus haute
        - calcule la moyenne arrondie à 2 décimales
        - construis la liste "au_dessus" des notes strictement
          supérieures à la moyenne, et affiche-la
    Indice : len(), min(), max() et sum() font le plus gros du travail.

Lancer :  python exercices.py
"""

print("--- EXERCICE 1 ---")

courses = ["pain", "lait", "oeufs"]


print()
print("--- EXERCICE 2 ---")

notes = [12, 15, 8, 19, 14, 11]
moyenne = None
au_dessus = []
