"""
CHAPITRE 04 — LES FONCTIONS

EXERCICE 1 — L'aire d'un rectangle
    Complète la fonction aire_rectangle pour qu'elle RENVOIE (return)
    l'aire d'un rectangle à partir de sa largeur et de sa hauteur.
    Attention : return, pas print. La fonction doit renvoyer une valeur
    utilisable, pas l'afficher.

EXERCICE 2 — Le calcul de TVA
    Complète la fonction prix_ttc pour qu'elle renvoie le prix TTC
    arrondi à 2 décimales :
        prix TTC = prix_ht + (prix_ht * taux / 100)
    Le paramètre taux vaut 20 par défaut : appeler prix_ttc(100) doit
    donner 120.0, et prix_ttc(100, 5.5) doit donner 105.5.
    Indice : round(3.14159, 2) donne 3.14

Lancer :  python exercices.py
"""

print("--- EXERCICE 1 ---")


def aire_rectangle(largeur, hauteur):
    """Renvoie l'aire d'un rectangle."""
    pass


print(aire_rectangle(4, 6))


print()
print("--- EXERCICE 2 ---")


def prix_ttc(prix_ht, taux=20):
    """Renvoie le prix TTC arrondi à 2 décimales."""
    pass


print(prix_ttc(100))
print(prix_ttc(100, 5.5))
