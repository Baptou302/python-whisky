# 06 — Les dictionnaires

## L'idée

Dans une liste, on retrouve les valeurs par leur **position** (`fruits[0]`).
Dans un **dictionnaire**, on les retrouve par un **nom** — qu'on appelle une **clé**.

```python
personne = {
    "prenom": "Lucas",
    "age": 25,
    "ville": "Lyon",
}

print(personne["prenom"])   # Lucas
```

C'est comme un vrai dictionnaire : un mot (la clé) → sa définition (la valeur).

- Accolades `{ }` (pas des crochets)
- Chaque entrée s'écrit `clé: valeur`
- Séparées par des virgules

---

## Liste ou dictionnaire ?

| Liste | Dictionnaire |
|-------|--------------|
| `["Lucas", 25, "Lyon"]` | `{"prenom": "Lucas", "age": 25, "ville": "Lyon"}` |
| Ordre important, accès par position | Accès par nom, beaucoup plus lisible |
| `personne[0]` — c'était quoi déjà, l'index 0 ? | `personne["prenom"]` — clair |

👉 Une liste pour **plusieurs choses du même genre**, un dictionnaire pour **décrire une chose**.

---

## Lire, modifier, ajouter, supprimer

```python
personne = {"prenom": "Lucas", "age": 25}

# Lire
print(personne["age"])          # 25
print(personne["taille"])       # 💥 KeyError : la clé n'existe pas

# Modifier
personne["age"] = 26

# Ajouter : on affecte simplement une nouvelle clé
personne["ville"] = "Lyon"

# Supprimer
del personne["ville"]
```

---

## `.get()` : lire sans risquer une erreur

```python
print(personne.get("taille"))            # None  (pas d'erreur)
print(personne.get("taille", "inconnu")) # inconnu  (valeur par défaut)
```

> 💡 Utilise `.get()` dès que tu n'es pas sûr que la clé existe.

---

## Tester la présence d'une clé

```python
if "age" in personne:
    print("On connaît son âge")
```

⚠️ `in` teste les **clés**, pas les valeurs.

---

## Parcourir un dictionnaire

```python
personne = {"prenom": "Lucas", "age": 25, "ville": "Lyon"}

# Les clés
for cle in personne:
    print(cle)                    # prenom, age, ville

# Les valeurs
for valeur in personne.values():
    print(valeur)                 # Lucas, 25, Lyon

# Les deux (le plus utile) :
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")
```

---

## Les méthodes utiles

```python
personne.keys()      # les clés
personne.values()    # les valeurs
personne.items()     # les paires (clé, valeur)
len(personne)        # le nombre d'entrées
personne.pop("age")  # supprime la clé et renvoie sa valeur
personne.clear()     # vide le dictionnaire
```

---

## Les règles sur les clés

- Une clé est **unique** : réaffecter la même clé écrase l'ancienne valeur
- Une clé doit être **immuable** : du texte ou un nombre (pas une liste)
- Les valeurs, elles, peuvent être **n'importe quoi** : nombres, textes, listes, autres dictionnaires...

---

## Structures imbriquées

C'est là que ça devient puissant. Un dictionnaire peut contenir des listes, et une liste peut contenir des dictionnaires.

```python
eleve = {
    "nom": "Marie",
    "notes": [15, 12, 18],          # une liste dans un dictionnaire
}
print(eleve["notes"][0])            # 15
print(sum(eleve["notes"]) / len(eleve["notes"]))   # moyenne


classe = [                          # une liste de dictionnaires
    {"nom": "Lucas", "note": 12},
    {"nom": "Marie", "note": 15},
]
for eleve in classe:
    print(f"{eleve['nom']} : {eleve['note']}")
```

> 💡 Attention aux guillemets dans les f-strings : si la f-string utilise `"`, utilise `'` à l'intérieur (`{eleve['nom']}`).

C'est exactement la forme des données que renvoient les API et les fichiers JSON. Bien maîtriser ça, c'est très utile.

---

## Un usage classique : compter des choses

```python
texte = "bonjour"
compteur = {}

for lettre in texte:
    if lettre in compteur:
        compteur[lettre] += 1
    else:
        compteur[lettre] = 1

print(compteur)   # {'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}

# Version courte avec .get() :
# compteur[lettre] = compteur.get(lettre, 0) + 1
```

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
