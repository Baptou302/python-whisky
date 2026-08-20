# 🐍 Python pour débutant total

Un parcours d'apprentissage de Python **en partant vraiment de zéro**.
Aucune connaissance en programmation n'est requise.

Chaque chapitre contient :

- un `README.md` qui explique la notion **avec des exemples** — c'est le cours
- un `exercices.py` avec **2 exercices**, dont les énoncés sont en haut du fichier
- un `solution.py` avec les corrigés

---

## 1. Installer Python

### Windows

1. Va sur [python.org/downloads](https://www.python.org/downloads/)
2. Télécharge la dernière version
3. **IMPORTANT** : pendant l'installation, coche la case **"Add Python to PATH"**

### macOS

```bash
brew install python
```

(ou télécharge l'installeur sur python.org)

### Linux

Python est déjà installé la plupart du temps. Sinon :

```bash
sudo apt install python3
```

### Vérifier que ça marche

Ouvre un terminal et tape :

```bash
python --version
```

Si ça affiche `Python 3.x.x`, c'est bon. Si la commande n'est pas trouvée, essaie `python3 --version`.

> Dans tout le repo, si `python` ne marche pas chez toi, remplace par `python3`.

---

## 2. Un éditeur de code

Je recommande **[VS Code](https://code.visualstudio.com/)** (gratuit) avec l'extension **Python** de Microsoft.

Alternative sans rien installer : [replit.com](https://replit.com) ou [Google Colab](https://colab.research.google.com) directement dans le navigateur.

---

## 3. Comment utiliser ce repo

1. Récupère le dossier sur ta machine
2. Ouvre-le dans VS Code
3. Commence par le chapitre `01-variables-et-types`
4. **Lis le `README.md`** du chapitre : c'est le cours, avec des exemples
5. Ouvre `exercices.py` : les **deux énoncés** sont écrits en haut du fichier
6. Écris ton code en dessous, puis lance le fichier :

```bash
python 01-variables-et-types/exercices.py
```

7. **Cherche d'abord**, galère un peu, c'est normal 🙂
8. Puis compare avec `solution.py`

> ⚠️ Ne regarde la solution qu'après avoir vraiment essayé. C'est en se cassant les dents qu'on apprend.

**Deux exercices par chapitre, pas plus.** L'idée n'est pas d'abattre du volume,
mais de bien comprendre chaque notion avant de passer à la suivante.

---

## 4. Le parcours

| # | Chapitre | Ce que tu vas apprendre |
|---|----------|--------------------------|
| 01 | [Variables et types](01-variables-et-types/) | Stocker des informations, les types de données |
| 02 | [Conditions](02-conditions/) | Faire des choix : `if` / `elif` / `else` |
| 03 | [Boucles](03-boucles/) | Répéter des actions : `for` et `while` |
| 04 | [Fonctions](04-fonctions/) | Créer ses propres outils réutilisables |
| 05 | [Listes](05-listes/) | Stocker plusieurs valeurs ensemble |
| 06 | [Dictionnaires](06-dictionnaires/) | Associer des clés à des valeurs |
| 07 | [Chaînes de caractères](07-chaines-de-caracteres/) | Manipuler du texte |
| 08 | [Fichiers](08-fichiers/) | Lire et écrire dans des fichiers |
| 09 | [Mini-projets](09-mini-projets/) | Tout mettre en pratique |

---

## 5. Checklist de progression

Coche au fur et à mesure 👇

- [ ] 01 - Variables et types
- [ ] 02 - Conditions
- [ ] 03 - Boucles
- [ ] 04 - Fonctions
- [ ] 05 - Listes
- [ ] 06 - Dictionnaires
- [ ] 07 - Chaînes de caractères
- [ ] 08 - Fichiers
- [ ] 09.1 - Mini-projet : Calculatrice
- [ ] 09.2 - Mini-projet : Jeu du pendu
- [ ] 09.3 - Mini-projet : Gestionnaire de tâches

---

## 6. Les erreurs, c'est normal

Tu vas voir plein de messages rouges. C'est **normal**, même les pros en voient tous les jours.

Les plus fréquentes au début :

| Erreur | Ça veut dire quoi ? |
|--------|---------------------|
| `SyntaxError` | Une faute de frappe : parenthèse ou guillemet oublié |
| `IndentationError` | Un problème d'espaces en début de ligne |
| `NameError` | Tu utilises une variable qui n'existe pas (faute de frappe ?) |
| `TypeError` | Tu mélanges des types incompatibles (ex: `"5" + 2`) |
| `ValueError` | La valeur ne convient pas (ex: `int("bonjour")`) |
| `IndexError` | Tu demandes un élément qui n'existe pas dans une liste |
| `KeyError` | Tu demandes une clé qui n'existe pas dans un dictionnaire |

👉 **Lis toujours la dernière ligne du message d'erreur**, c'est celle qui explique le problème.

---

## 7. Pour aller plus loin

- [Documentation officielle Python (FR)](https://docs.python.org/fr/3/)
- [Exercism - Python](https://exercism.org/tracks/python) : plein d'exercices gratuits
- [Advent of Code](https://adventofcode.com/) : des puzzles de code (dur mais fun)

Bon courage 💪
