"""
CHAPITRE 08 — LIRE ET ÉCRIRE DES FICHIERS

Les fichiers de travail sont dans le sous-dossier donnees/.
Les deux lignes os.chdir(...) placent Python dans le dossier de ce
fichier, pour que les chemins "donnees/..." marchent d'où que tu
lances le script. Ne les touche pas.

EXERCICE 1 — Lire un fichier
    Ouvre donnees/citations.txt en lecture et affiche chaque citation
    numérotée, une par ligne :
        1. La simplicité est la sophistication suprême.
        2. Le code est lu bien plus souvent qu'il n'est écrit.
        ...
    Indices : "with open(chemin, "r", encoding="utf-8") as f:" ouvre le
    fichier, on peut ensuite boucler dessus ligne par ligne, et .strip()
    enlève le retour à la ligne de fin.

EXERCICE 2 — Analyser un CSV et écrire un rapport
    donnees/notes.csv contient trois colonnes : prenom,matiere,note
    La première ligne contient les en-têtes, il faut l'ignorer.
    Calcule la moyenne de chaque élève, affiche-la, puis écris un
    fichier rapport.txt contenant une ligne par élève :
        Lucas : 13.5
        Marie : 15.5
        ...
    Indices : ligne.strip().split(",") découpe une ligne en trois
    morceaux. Construis un dictionnaire {prenom: [notes]} au passage.
    N'oublie pas int() : tout ce qui vient d'un fichier est du texte.
    Pour écrire, ouvre le fichier en mode "w" et n'oublie pas d'ajouter
    toi-même le retour à la ligne à la fin de chaque ligne écrite.

Lancer :  python exercices.py
"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


print("--- EXERCICE 1 ---")


print()
print("--- EXERCICE 2 ---")

notes_par_eleve = {}
