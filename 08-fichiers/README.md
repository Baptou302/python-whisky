# 08 — Lire et écrire des fichiers

Jusqu'ici, tout disparaissait à la fin du programme. Avec les fichiers, on peut **garder** les données.

---

## Lire un fichier

```python
with open("mon_fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

print(contenu)
```

Décortiquons :

| Morceau | Rôle |
|---------|------|
| `open(...)` | ouvre le fichier |
| `"r"` | mode **read** (lecture) |
| `encoding="utf-8"` | pour que les accents ne cassent pas |
| `with ... as f` | ferme automatiquement le fichier à la fin du bloc |
| `f.read()` | lit tout le contenu d'un coup, sous forme de texte |

> 💡 **Utilise toujours `with`.** Sans lui, il faudrait penser à faire `f.close()`,
> et si une erreur survient entre-temps le fichier reste ouvert.

---

## Les trois façons de lire

```python
with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()          # tout, en une seule chaîne

with open("fichier.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()      # une LISTE, une entrée par ligne

with open("fichier.txt", "r", encoding="utf-8") as f:
    for ligne in f:             # ligne par ligne (le plus économe en mémoire)
        print(ligne.strip())
```

> ⚠️ Chaque ligne lue se termine par un `\n` (retour à la ligne).
> D'où le `.strip()` un peu partout, pour l'enlever.

---

## Écrire dans un fichier

```python
# "w" = write : ÉCRASE tout le contenu existant !
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")

# "a" = append : AJOUTE à la fin sans rien effacer
with open("sortie.txt", "a", encoding="utf-8") as f:
    f.write("Une ligne de plus\n")
```

| Mode | Effet |
|------|-------|
| `"r"` | lecture (erreur si le fichier n'existe pas) |
| `"w"` | écriture — **écrase tout**, crée le fichier s'il n'existe pas |
| `"a"` | ajout à la fin, crée le fichier s'il n'existe pas |

> 🚨 `"w"` sur un fichier existant efface son contenu **immédiatement**. Fais attention.

`f.write()` ne va **pas** à la ligne tout seul : il faut mettre `\n` toi-même.

---

## Gérer les erreurs

Que se passe-t-il si le fichier n'existe pas ? Le programme plante.
Pour éviter ça, on utilise `try` / `except` :

```python
try:
    with open("inexistant.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Le fichier n'existe pas !")
```

Le principe : *essaie* (`try`) ce bloc ; si l'erreur indiquée survient, *fais plutôt* (`except`) ceci.

Pour vérifier avant d'ouvrir :

```python
import os

if os.path.exists("mon_fichier.txt"):
    print("Le fichier existe")
```

---

## Les chemins de fichiers

- `"notes.txt"` → dans le dossier depuis lequel tu lances le programme
- `"donnees/notes.txt"` → dans le sous-dossier `donnees`
- `"../notes.txt"` → dans le dossier parent

> ⚠️ Le chemin est relatif au dossier **depuis lequel tu lances Python**, pas au dossier du fichier `.py`.
> C'est une source de confusion classique. Dans les exercices, on règle ça avec deux lignes
> au début du fichier (`os.chdir(...)`) pour que ça marche d'où que tu le lances.

---

## Le format CSV

Un fichier CSV, c'est un tableau en texte brut : une ligne par enregistrement, des colonnes séparées par des virgules.

```
prenom,matiere,note
Lucas,maths,12
Marie,maths,17
```

On peut le lire à la main avec `.split(",")` (c'est ce qu'on fait dans les exercices, pour comprendre),
mais Python a un module dédié :

```python
import csv

with open("notes.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne["prenom"], ligne["note"])   # chaque ligne est un dictionnaire
```

---

## Bonus : le JSON

Pour sauvegarder des dictionnaires et des listes tels quels, JSON est le format idéal :

```python
import json

donnees = {"nom": "Lucas", "notes": [12, 15, 18]}

# Sauvegarder
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=2, ensure_ascii=False)

# Recharger
with open("data.json", "r", encoding="utf-8") as f:
    donnees = json.load(f)

print(donnees["notes"])   # [12, 15, 18]
```

C'est ce qu'on utilisera dans le mini-projet "gestionnaire de tâches".

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
