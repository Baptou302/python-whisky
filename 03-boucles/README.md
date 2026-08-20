# 03 — Les boucles

## Pourquoi ?

Imagine que tu veuilles afficher les nombres de 1 à 100. Tu ne vas pas écrire 100 `print()`.
Les **boucles** servent à répéter des actions.

Il y en a deux : `for` et `while`.

---

## La boucle `for` : "pour chaque..."

```python
for i in range(5):
    print(i)
```

Affiche :

```
0
1
2
3
4
```

Traduction en français : *"pour chaque nombre `i` dans la séquence 0,1,2,3,4 : affiche `i`"*.

Comme pour le `if` : **deux-points `:`** et **indentation** du bloc.

---

## `range()` : générer une séquence de nombres

`range()` s'utilise de 3 façons :

```python
range(5)         # 0, 1, 2, 3, 4        -> de 0 à 5 EXCLU
range(2, 6)      # 2, 3, 4, 5           -> de 2 à 6 EXCLU
range(0, 10, 2)  # 0, 2, 4, 6, 8        -> de 0 à 10, par pas de 2
range(5, 0, -1)  # 5, 4, 3, 2, 1        -> à l'envers
```

> 🚨 **La borne de fin est toujours exclue.** `range(1, 11)` donne bien 1 à 10.
> C'est l'une des sources d'erreur les plus fréquentes.

---

## Parcourir autre chose que des nombres

`for` marche aussi sur du texte et sur des listes (chapitre 05) :

```python
for lettre in "chat":
    print(lettre)
# c, h, a, t

for fruit in ["pomme", "poire", "banane"]:
    print(fruit)
```

---

## La variable d'accumulation

Un motif que tu vas utiliser tout le temps : préparer une variable **avant** la boucle,
et la modifier **à chaque tour**.

```python
total = 0                  # on part de 0
for i in range(1, 6):      # 1, 2, 3, 4, 5
    total = total + i      # à chaque tour on ajoute i
print(total)               # 15
```

Raccourcis très utilisés :

```python
total += i    # équivaut à  total = total + i
total -= 1    # équivaut à  total = total - 1
total *= 2    # équivaut à  total = total * 2
```

---

## La boucle `while` : "tant que..."

`while` répète **tant qu'une condition est vraie** :

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

> 🚨 **Attention aux boucles infinies !**
> Si tu oublies le `compteur += 1`, la condition reste vraie pour toujours et ton programme
> ne s'arrête jamais. Dans ce cas : `Ctrl + C` dans le terminal.

---

## `for` ou `while` ?

| Utilise... | Quand... |
|-----------|----------|
| `for` | tu sais combien de fois répéter (ou tu parcours une séquence) |
| `while` | tu répètes jusqu'à ce qu'un truc arrive (ex: l'utilisateur tape "stop") |

Dans le doute, `for` est plus sûr : impossible de faire une boucle infinie.

---

## `break` et `continue`

```python
# break : sortir de la boucle immédiatement
for i in range(10):
    if i == 5:
        break
    print(i)      # affiche 0,1,2,3,4 puis s'arrête

# continue : sauter au tour suivant
for i in range(5):
    if i == 2:
        continue
    print(i)      # affiche 0,1,3,4 (le 2 est sauté)
```

---

## Boucles imbriquées

Une boucle dans une boucle. La boucle intérieure fait un tour **complet** à chaque tour de l'extérieure.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
```

---

## Petit truc pratique : `end=`

Par défaut, `print()` va à la ligne. Pour rester sur la même ligne :

```python
for i in range(5):
    print(i, end=" ")
print()   # pour aller à la ligne à la fin
# affiche : 0 1 2 3 4
```

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
