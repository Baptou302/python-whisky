# 09 — Les mini-projets

Bravo, tu as fait tous les chapitres 🎉

Maintenant on passe à la partie la plus intéressante : **construire de vrais petits programmes**.
C'est là que tout se met en place.

---

## Comment aborder un projet

C'est différent d'un exercice : personne ne te dit quoi écrire ligne par ligne.
La méthode qui marche :

1. **Lis le cahier des charges** en entier
2. **Découpe** le problème en petits morceaux (une fonction par morceau)
3. **Fais marcher un truc minuscule d'abord**, puis ajoute
4. **Teste souvent** — lance ton code toutes les 5 lignes, pas à la fin
5. Bloqué plus de 20 minutes ? Regarde la solution, comprends-la, puis **referme-la et réécris-la**

> 💡 Le `starter.py` te donne le squelette et l'ordre des étapes. Commence par là.

---

## Les projets

| # | Projet | Notions utilisées | Difficulté |
|---|--------|-------------------|------------|
| 01 | [Calculatrice](01-calculatrice/) | fonctions, conditions, boucle while, input | ⭐ |
| 02 | [Jeu du pendu](02-jeu-du-pendu/) | listes, boucles, chaînes, random | ⭐⭐ |
| 03 | [Gestionnaire de tâches](03-gestionnaire-de-taches/) | dictionnaires, listes, fichiers, JSON | ⭐⭐⭐ |

Fais-les dans l'ordre, la difficulté monte progressivement.

---

## Petit rappel : `input()`

Contrairement aux chapitres, ici les programmes sont **interactifs**. Rappel :

```python
reponse = input("Ton choix : ")     # renvoie toujours du TEXTE
nombre = int(input("Un nombre : ")) # à convertir si tu veux un nombre
```

Et pour ne pas planter si l'utilisateur tape n'importe quoi :

```python
saisie = input("Un nombre : ")
if saisie.isdigit():
    nombre = int(saisie)
else:
    print("Ce n'est pas un nombre !")
```

---

## Et après ?

Quelques idées pour continuer tout seul :

- Un **quiz** à choix multiples qui garde les scores
- Un **convertisseur d'unités** (km/miles, °C/°F, euros/dollars)
- Un **générateur de mots de passe**
- Un **carnet d'adresses** avec recherche
- Le jeu du **plus ou moins** (deviner un nombre entre 1 et 100)
- Un **compteur de calories** qui sauvegarde dans un fichier

Le meilleur moyen de progresser, c'est de coder un truc **qui te sert vraiment**.
