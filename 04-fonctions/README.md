# 04 — Les fonctions

## L'idée

Une fonction, c'est un **bout de code auquel on donne un nom**, pour pouvoir le réutiliser
autant de fois qu'on veut sans le réécrire.

Tu en utilises déjà : `print()`, `len()`, `int()`, `range()`... Maintenant tu vas créer les tiennes.

---

## Définir et appeler une fonction

```python
def dire_bonjour():
    print("Bonjour !")
    print("Comment ça va ?")

dire_bonjour()   # on APPELLE la fonction -> le code s'exécute
dire_bonjour()   # on peut la rappeler autant qu'on veut
```

- `def` = *define*, on **définit** la fonction
- Ne pas oublier les **parenthèses** et les **deux-points**
- Le corps de la fonction est **indenté**

> ⚠️ Définir une fonction ne l'exécute pas. Il faut **l'appeler** avec `nom_de_la_fonction()`.

---

## Les paramètres : donner des infos à la fonction

```python
def dire_bonjour(prenom):
    print(f"Bonjour {prenom} !")

dire_bonjour("Lucas")   # Bonjour Lucas !
dire_bonjour("Marie")   # Bonjour Marie !
```

`prenom` est un **paramètre** : une variable qui existe uniquement à l'intérieur de la fonction.

Plusieurs paramètres ? On les sépare par des virgules :

```python
def presenter(prenom, age):
    print(f"{prenom} a {age} ans")

presenter("Lucas", 25)
```

⚠️ **L'ordre compte** : `presenter(25, "Lucas")` donnerait n'importe quoi.

---

## `return` : récupérer un résultat

C'est la partie la plus importante — et celle qui pose le plus de problèmes au début.

```python
def addition(a, b):
    return a + b

resultat = addition(3, 5)
print(resultat)          # 8
print(addition(10, 20))  # 30
```

`return` **renvoie** une valeur à celui qui a appelé la fonction.

### `print` ≠ `return`

```python
def addition_print(a, b):
    print(a + b)         # AFFICHE le résultat

def addition_return(a, b):
    return a + b         # RENVOIE le résultat

x = addition_print(2, 3)   # affiche 5, mais x vaut None !
y = addition_return(2, 3)  # n'affiche rien, mais y vaut 5 ✅
```

👉 **Règle simple** : si tu veux réutiliser le résultat plus tard, il faut `return`.

### `return` arrête la fonction

```python
def valeur_absolue(n):
    if n < 0:
        return -n     # si on passe ici, la fonction s'arrête ici
    return n
```

Une fonction sans `return` renvoie `None`.

---

## Les paramètres par défaut

```python
def saluer(prenom, message="Bonjour"):
    print(f"{message} {prenom} !")

saluer("Lucas")             # Bonjour Lucas !
saluer("Lucas", "Salut")    # Salut Lucas !
```

⚠️ Les paramètres avec une valeur par défaut doivent être **à la fin**.

---

## Les arguments nommés

Pour plus de clarté, on peut préciser le nom du paramètre :

```python
def creer_profil(prenom, age, ville):
    print(f"{prenom}, {age} ans, {ville}")

creer_profil(age=25, ville="Lyon", prenom="Lucas")   # l'ordre n'a plus d'importance
```

---

## La portée des variables (*scope*)

Une variable créée **dans** une fonction n'existe **que** dans cette fonction :

```python
def ma_fonction():
    secret = 42
    print(secret)   # ✅ marche

ma_fonction()
print(secret)       # 💥 NameError : secret n'existe pas ici
```

C'est une bonne chose : ça évite que tes fonctions se marchent dessus.

---

## La docstring

Un texte entre triple guillemets juste après le `def` explique ce que fait la fonction :

```python
def aire_rectangle(largeur, hauteur):
    """Calcule l'aire d'un rectangle."""
    return largeur * hauteur
```

Ce n'est pas obligatoire, mais c'est une très bonne habitude.

---

## Pourquoi c'est important ?

1. **Ne pas se répéter** : écris le code une fois, réutilise-le partout
2. **Corriger à un seul endroit** : un bug ? Tu le corriges dans la fonction, c'est réglé partout
3. **Lisibilité** : `calculer_tva(prix)` se comprend mieux que 5 lignes de calcul
4. **Découper** : un gros problème devient plein de petits problèmes faciles

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
