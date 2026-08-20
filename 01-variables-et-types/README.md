# 01 — Variables et types

## C'est quoi une variable ?

Une variable, c'est une **boîte avec une étiquette** dans laquelle on range une valeur.

```python
age = 25
```

Ici on crée une boîte étiquetée `age` qui contient `25`.
On peut ensuite réutiliser la boîte partout :

```python
age = 25
print(age)      # affiche 25
print(age + 5)  # affiche 30
```

Le signe `=` ne veut **pas** dire "égal" comme en maths. Il veut dire **"range la valeur de droite dans la boîte de gauche"**.

On peut changer le contenu d'une boîte quand on veut :

```python
age = 25
age = 30
print(age)  # affiche 30
```

---

## `print()` : afficher quelque chose

`print()` affiche un truc dans le terminal. C'est ton meilleur ami pour comprendre ce qui se passe.

```python
print("Bonjour")       # Bonjour
print(42)              # 42
print("Age :", 25)     # Age : 25
```

---

## Les 4 types de base

| Type | Nom Python | Exemple | À quoi ça sert |
|------|-----------|---------|----------------|
| Texte | `str` | `"bonjour"` | Du texte, entre guillemets |
| Nombre entier | `int` | `42` | Des nombres sans virgule |
| Nombre décimal | `float` | `3.14` | Des nombres à virgule (⚠️ **point**, pas virgule) |
| Booléen | `bool` | `True` / `False` | Vrai ou faux |

```python
prenom = "Lucas"      # str
age = 25              # int
taille = 1.82         # float
majeur = True         # bool
```

Pour connaître le type d'une variable :

```python
print(type(age))  # <class 'int'>
```

---

## Les guillemets

Pour le texte, simples `'` ou doubles `"`, au choix — mais il faut **fermer avec le même** :

```python
a = "bonjour"
b = 'bonjour'   # pareil
c = "j'ai faim" # pratique : guillemets doubles quand il y a une apostrophe
```

---

## Les opérations sur les nombres

```python
print(10 + 3)   # 13   addition
print(10 - 3)   # 7    soustraction
print(10 * 3)   # 30   multiplication
print(10 / 3)   # 3.333...  division (donne toujours un float)
print(10 // 3)  # 3    division entière (on garde juste la partie entière)
print(10 % 3)   # 1    modulo = le RESTE de la division
print(10 ** 3)  # 1000 puissance (10 puissance 3)
```

> 💡 Le **modulo** `%` est super utile : `n % 2 == 0` permet de savoir si `n` est pair.

---

## Attention : texte ≠ nombre

```python
print("5" + "3")   # 53   ← concaténation de texte !
print(5 + 3)       # 8    ← vraie addition
print("5" + 3)     # 💥 TypeError
```

Le `+` colle les textes ensemble, et additionne les nombres. Il faut donc **convertir** :

```python
int("5")      # 5      texte → entier
float("3.5")  # 3.5    texte → décimal
str(5)        # "5"    nombre → texte
```

---

## Les f-strings : afficher proprement

Mets un `f` juste avant le guillemet d'ouverture, puis des `{}` autour des variables :

```python
prenom = "Lucas"
age = 25

print(f"Je m'appelle {prenom} et j'ai {age} ans.")
# Je m'appelle Lucas et j'ai 25 ans.

print(f"Dans 10 ans j'aurai {age + 10} ans.")
# Dans 10 ans j'aurai 35 ans.
```

C'est **la** façon moderne de faire, utilise ça partout.

---

## `input()` : demander un truc à l'utilisateur

```python
prenom = input("Quel est ton prénom ? ")
print(f"Salut {prenom} !")
```

⚠️ **`input()` renvoie TOUJOURS du texte**, même si l'utilisateur tape un nombre :

```python
age = input("Ton âge ? ")     # si l'user tape 25, age vaut "25" (du TEXTE)
age = int(age)                # maintenant age vaut 25 (un NOMBRE)

# ou en une ligne :
age = int(input("Ton âge ? "))
```

> Dans les exercices de ce chapitre on n'utilise pas `input()`, pour que tu puisses lancer le fichier d'un coup. On s'en servira dans les mini-projets.

---

## Les commentaires

Tout ce qui suit un `#` est ignoré par Python. C'est pour expliquer ton code.

```python
# Ceci est un commentaire
age = 25  # on peut aussi en mettre en fin de ligne
```

---

## Règles pour nommer une variable

✅ `age`, `mon_age`, `prix_total`, `nombre2`
❌ `2nombre` (ne peut pas commencer par un chiffre)
❌ `mon age` (pas d'espace)
❌ `prix-total` (pas de tiret, Python croit que c'est une soustraction)

Convention Python : **tout en minuscules, mots séparés par des `_`** (on appelle ça le *snake_case*).

💡 Donne des noms qui veulent dire quelque chose : `prix_total` plutôt que `x`.

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
