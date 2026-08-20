"""
MINI-PROJET 03 — LE GESTIONNAIRE DE TÂCHES

Le cahier des charges complet est dans le README.md.
Complète les fonctions dans l'ordre, et lance le programme après
chacune pour tester.

Les deux lignes os.chdir(...) placent Python dans le dossier de ce
fichier, pour que taches.json soit toujours créé au bon endroit.

Lancer :  python starter.py
"""

import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FICHIER = "taches.json"


def charger_taches():
    """
    Lit FICHIER et renvoie la liste des tâches qu'il contient.

    Au tout premier lancement le fichier n'existe pas encore : il faut
    renvoyer une liste vide plutôt que planter. Utilise un bloc try
    avec un except FileNotFoundError.
    json.load(f) transforme le contenu du fichier en objet Python.
    """
    pass


def sauvegarder_taches(taches):
    """
    Écrit la liste des tâches dans FICHIER, en mode "w".

    json.dump(taches, f, indent=2, ensure_ascii=False) produit un
    fichier lisible et conserve les accents.
    """
    pass


def afficher_taches(taches):
    """
    Affiche les tâches numérotées à partir de 1.

    Si la liste est vide, affiche un message et arrête-toi là.
    Sinon, affiche chaque tâche sous la forme "  1. [ ] Titre", avec
    [x] quand la tâche est terminée. Termine par le nombre de tâches
    terminées sur le total.
    """
    pass


def ajouter_tache(taches):
    """
    Demande un titre et ajoute la tâche à la liste.

    Refuse un titre vide. Une tâche est un dictionnaire de la forme
    {"titre": ..., "terminee": False}. Ajoute-le avec .append() puis
    sauvegarde immédiatement.
    """
    pass


def demander_numero(taches):
    """
    Demande un numéro de tâche et renvoie l'index correspondant.

    Renvoie None si la liste est vide, si la saisie n'est pas un
    nombre, ou si le numéro ne correspond à aucune tâche.
    Le joueur voit 1, 2, 3 mais Python indexe 0, 1, 2 : renvoie donc
    le numéro moins un.
    """
    pass


def terminer_tache(taches):
    """
    Passe une tâche à l'état terminé.

    Récupère l'index avec demander_numero, arrête-toi s'il vaut None,
    sinon mets la clé "terminee" à True et sauvegarde.
    """
    pass


def supprimer_tache(taches):
    """
    Retire une tâche de la liste.

    Même principe que terminer_tache, avec .pop(index) qui retire
    l'élément et le renvoie.
    """
    pass


def main():
    """
    Menu principal.

    Charge les tâches, puis répète indéfiniment : afficher les tâches,
    afficher le menu, lire le choix et appeler la fonction
    correspondante. Sortir avec break sur le choix Quitter.
    """
    print("=" * 33)
    print("   GESTIONNAIRE DE TÂCHES")
    print("=" * 33)

    taches = charger_taches()

    print("\nÀ bientôt !")


if __name__ == "__main__":
    main()
