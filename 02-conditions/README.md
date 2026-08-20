# 02 — Les conditions

## L'idée

Jusqu'ici, ton code s'exécutait ligne par ligne, du haut vers le bas, toujours pareil.
Les **conditions** permettent de dire : *"si telle chose est vraie, fais ça"*.

```python
age = 20

if age >= 18:
    print("Tu es majeur")
```

---

## La syntaxe (attention, c'est important)

```python
if condition:
    # code exécuté SI la condition est vraie
```

Deux choses à ne **jamais** oublier :

1. Les **deux-points `:`** à la fin de la ligne du `if`
2. L'**indentation** : le code à l'intérieur du `if` est décalé de 4 espaces

```python
if age >= 18:
    print("A")      # DANS le if
    print("B")      # DANS le if aussi
print("C")          # HORS du if : s'affiche toujours
```

> En Python, l'indentation n'est pas de la décoration : **c'est elle qui définit les blocs**.
> Dans VS Code, la touche `Tab` fait les 4 espaces pour toi.

---

## `else` : sinon

```python
age = 15

if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")
```

---

## `elif` : sinon si

Pour tester plusieurs cas à la suite :

```python
note = 14

if note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

⚠️ Python teste **de haut en bas** et s'arrête au **premier cas vrai**.
L'ordre compte énormément : si tu mets `note >= 10` en premier, une note de 18 affichera "Passable".

---

## Les opérateurs de comparaison

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `==` | est égal à | `age == 18` |
| `!=` | est différent de | `age != 18` |
| `>` | est supérieur à | `age > 18` |
| `<` | est inférieur à | `age < 18` |
| `>=` | supérieur ou égal | `age >= 18` |
| `<=` | inférieur ou égal | `age <= 18` |

> 🚨 **L'erreur n°1 des débutants** : confondre `=` et `==`.
> - `=` **range** une valeur : `age = 18`
> - `==` **compare** : `age == 18`

Une comparaison produit toujours `True` ou `False` :

```python
print(5 > 3)    # True
print(5 == 3)   # False
```

---

## Combiner des conditions : `and`, `or`, `not`

```python
age = 25
permis = True

# and : il faut que LES DEUX soient vraies
if age >= 18 and permis:
    print("Tu peux conduire")

# or : il suffit qu'UNE des deux soit vraie
if age < 18 or not permis:
    print("Tu ne peux pas conduire")
```

| Opérateur | Vrai quand... |
|-----------|---------------|
| `A and B` | A **et** B sont vrais |
| `A or B` | A **ou** B est vrai (ou les deux) |
| `not A` | A est faux |

Python permet aussi cette écriture très pratique :

```python
if 0 <= note <= 20:
    print("Note valide")
```

---

## Conditions imbriquées

Un `if` peut contenir un autre `if` :

```python
if age >= 18:
    if permis:
        print("Tu peux conduire")
    else:
        print("Majeur, mais pas de permis")
else:
    print("Trop jeune")
```

💡 Souvent, un `and` est plus lisible qu'un `if` imbriqué. Préfère le `and` quand c'est possible.

---

## Ce qui est considéré comme "faux"

Dans un `if`, ces valeurs comptent comme `False` :

```python
False, 0, 0.0, "", [], {}, None
```

Tout le reste compte comme `True`. Donc :

```python
prenom = ""
if prenom:
    print("Bonjour")
else:
    print("Tu n'as pas donné ton prénom")   # c'est ce qui s'affiche
```

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
