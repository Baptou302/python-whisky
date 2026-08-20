"""
MINI-PROJET 02 — LE JEU DU PENDU

Le cahier des charges complet est dans le README.md.
Complète les fonctions dans l'ordre où elles apparaissent, et lance
le programme après chacune pour tester.

Lancer :  python starter.py
"""

import random

MOTS = [
    "python", "ordinateur", "clavier", "programme", "variable",
    "fonction", "boucle", "fichier", "liste", "dictionnaire",
]

MAX_ERREURS = 7


def choisir_mot():
    """Renvoie un mot au hasard parmi MOTS, grâce à random.choice."""
    pass


def afficher_mot(mot, lettres_trouvees):
    """
    Renvoie le mot avec un _ à la place de chaque lettre non trouvée.

    afficher_mot("chat", ["c", "t"]) doit renvoyer "c _ _ t".
    Construis une liste au fur et à mesure, puis assemble-la avec
    " ".join(...) pour séparer les caractères par des espaces.
    """
    pass


def demander_lettre(lettres_proposees):
    """
    Demande une lettre au joueur et la renvoie en minuscule.

    Redemande si la saisie ne fait pas exactement un caractère, si ce
    n'est pas une lettre, ou si elle figure déjà dans lettres_proposees.
    Les méthodes utiles ici sont len(), .isalpha() et l'opérateur "in".
    """
    pass


def mot_trouve(mot, lettres_trouvees):
    """
    Renvoie True si toutes les lettres du mot ont été trouvées.

    Il suffit qu'une seule lettre manque pour renvoyer False.
    """
    pass


def dessiner_pendu(erreurs):
    """
    Affiche le dessin correspondant au nombre d'erreurs.

    À faire en dernier, une fois que le jeu fonctionne. Crée une liste
    de MAX_ERREURS + 1 dessins et affiche celui d'index erreurs.
    """
    pass


def main():
    """
    Boucle de jeu.

    Tire un mot, puis répète tant que le nombre d'erreurs est inférieur
    à MAX_ERREURS : afficher l'état de la partie, demander une lettre,
    l'ajouter aux lettres proposées, puis soit l'ajouter aux lettres
    trouvées, soit incrémenter le compteur d'erreurs. Sortir avec break
    dès que le mot est trouvé. Après la boucle, annoncer la défaite et
    révéler le mot.
    """
    print("=" * 25)
    print("    LE JEU DU PENDU")
    print("=" * 25)

    mot = choisir_mot()
    lettres_trouvees = []
    lettres_proposees = []
    erreurs = 0


if __name__ == "__main__":
    main()
