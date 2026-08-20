"""
CHAPITRE 02 — LES CONDITIONS

EXERCICE 1 — Les mentions au bac
    Selon la valeur de note, affiche la mention correspondante :
        note >= 16  ->  "Très bien"
        note >= 14  ->  "Bien"
        note >= 12  ->  "Assez bien"
        note >= 10  ->  "Passable"
        sinon       ->  "Recalé"
    Utilise if / elif / else. Attention à l'ordre des conditions.

EXERCICE 2 — Le prix du ticket de cinéma
    Calcule le prix dans une variable prix, puis affiche-le.
        moins de 12 ans           ->  5 euros
        étudiant (quel que soit l'âge)  ->  7 euros
        65 ans et plus            ->  6 euros
        sinon                     ->  11 euros
    L'ordre de tes conditions détermine qui a la priorité : réfléchis
    à ce que doit payer un étudiant de 66 ans.

Lancer :  python exercices.py
"""

print("--- EXERCICE 1 ---")

note = 15


print()
print("--- EXERCICE 2 ---")

age = 30
etudiant = False
prix = None
