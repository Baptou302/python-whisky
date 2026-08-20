# 05 — Les listes

## L'idée

Une variable classique ne stocke qu'une valeur. Une **liste** en stocke plusieurs, dans l'ordre.

```python
fruits = ["pomme", "poire", "banane"]
notes = [12, 15, 8, 19]
melange = ["Lucas", 25, 1.82, True]   # possible, mais rare en pratique
vide = []
```

Crochets `[ ]`, valeurs séparées par des virgules.

---

## Accéder à un élément : les index

**On compte à partir de 0.** C'est la règle qui déroute tout le monde au début.

```python
fruits = ["pomme", "poire", "banane"]
#            0        1        2
#           -3       -2       -1

print(fruits[0])    # pomme
print(fruits[2])    # banane
print(fruits[-1])   # banane  (le dernier)
print(fruits[-2])   # poire   (l'avant-dernier)
print(fruits[3])    # 💥 IndexError : il n'y a pas d'index 3
```

Les index négatifs partent de la fin : `-1` est **toujours** le dernier élément.

---

## Modifier un élément

```python
fruits[1] = "kiwi"
print(fruits)   # ['pomme', 'kiwi', 'banane']
```

---

## La longueur : `len()`

```python
print(len(fruits))       # 3
print(fruits[len(fruits) - 1])   # le dernier (mais fruits[-1] est plus simple)
```

---

## Les méthodes utiles

Une "méthode" s'écrit `ma_liste.quelquechose()` :

```python
fruits = ["pomme", "poire"]

fruits.append("banane")        # ajoute à la FIN         -> ['pomme','poire','banane']
fruits.insert(0, "kiwi")       # insère à l'index 0      -> ['kiwi','pomme','poire','banane']
fruits.remove("poire")         # supprime PAR VALEUR     -> ['kiwi','pomme','banane']
dernier = fruits.pop()         # retire ET renvoie le dernier
fruits.sort()                  # trie la liste sur place
fruits.reverse()               # inverse l'ordre
print(fruits.count("kiwi"))    # combien de fois "kiwi" apparaît
print(fruits.index("pomme"))   # à quel index se trouve "pomme"
fruits.clear()                 # vide la liste
```

Et sur des listes de nombres :

```python
notes = [12, 15, 8, 19]
print(len(notes))    # 4
print(sum(notes))    # 54   la somme
print(min(notes))    # 8    le plus petit
print(max(notes))    # 19   le plus grand
print(sorted(notes)) # [8, 12, 15, 19]  -> nouvelle liste triée, l'originale ne bouge pas
```

> 💡 `notes.sort()` **modifie** la liste. `sorted(notes)` en **crée une nouvelle**. C'est une distinction utile.

---

## Parcourir une liste

```python
fruits = ["pomme", "poire", "banane"]

# La façon normale :
for fruit in fruits:
    print(fruit)

# Avec l'index en plus :
for i, fruit in enumerate(fruits):
    print(f"{i} : {fruit}")
# 0 : pomme
# 1 : poire
# 2 : banane
```

---

## Tester la présence : `in`

```python
if "pomme" in fruits:
    print("On a des pommes")

if "kiwi" not in fruits:
    print("Pas de kiwi")
```

---

## Le *slicing* : découper une liste

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nombres[2:5])    # [2, 3, 4]      de l'index 2 à 5 EXCLU
print(nombres[:3])     # [0, 1, 2]      depuis le début
print(nombres[7:])     # [7, 8, 9]      jusqu'à la fin
print(nombres[::2])    # [0,2,4,6,8]    un sur deux
print(nombres[::-1])   # [9,8,...,0]    à l'envers
print(nombres[:])      # une COPIE de la liste
```

---

## ⚠️ Le piège de la copie

```python
a = [1, 2, 3]
b = a            # b n'est PAS une copie : c'est la MÊME liste !
b.append(4)
print(a)         # [1, 2, 3, 4]  ← a a changé aussi !

# Pour vraiment copier :
b = a.copy()     # ou a[:]  ou list(a)
```

C'est une source de bugs classique. Retiens-le.

---

## Les *list comprehensions* (bonus)

Une façon compacte de créer une liste. Tu croiseras ça partout en Python :

```python
carres = [n * n for n in range(5)]          # [0, 1, 4, 9, 16]
pairs = [n for n in range(10) if n % 2 == 0] # [0, 2, 4, 6, 8]
```

Ça remplace :

```python
carres = []
for n in range(5):
    carres.append(n * n)
```

Pas obligatoire au début, mais bon à reconnaître.

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
