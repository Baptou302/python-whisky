# 07 — Les chaînes de caractères

Une "chaîne de caractères" (*string*, ou `str`), c'est simplement du **texte**.
Tu en manipules depuis le chapitre 01 — voici tout ce qu'on peut en faire.

---

## Une chaîne, c'est une suite de caractères

Comme une liste, on peut y accéder par index et la découper :

```python
mot = "Python"
#      012345

print(mot[0])     # P
print(mot[-1])    # n
print(mot[0:3])   # Pyt
print(mot[::-1])  # nohtyP   (à l'envers)
print(len(mot))   # 6

for lettre in mot:
    print(lettre)
```

> ⚠️ Grosse différence avec les listes : **une chaîne est immuable**.
> `mot[0] = "J"` provoque une erreur. Pour "modifier" une chaîne, on en crée une nouvelle.

---

## Les méthodes essentielles

```python
texte = "  Bonjour le Monde  "

texte.strip()          # "Bonjour le Monde"   enlève les espaces au début/fin
texte.lower()          # "  bonjour le monde  "  tout en minuscules
texte.upper()          # "  BONJOUR LE MONDE  "  tout en majuscules
texte.replace("o", "0")# remplace tous les "o" par des "0"
texte.count("o")       # combien de "o"
texte.find("Monde")    # l'index où commence "Monde" (-1 si absent)
```

⚠️ **Ces méthodes ne modifient rien**, elles **renvoient une nouvelle chaîne** :

```python
texte = "bonjour"
texte.upper()          # ne change PAS texte
print(texte)           # bonjour

texte = texte.upper()  # ✅ il faut réaffecter
print(texte)           # BONJOUR
```

---

## `split()` et `join()` : le duo indispensable

```python
# split : texte -> liste
phrase = "le chat mange la souris"
mots = phrase.split()            # ['le','chat','mange','la','souris']

csv = "Lucas,25,Lyon"
infos = csv.split(",")           # ['Lucas', '25', 'Lyon']

# join : liste -> texte
mots = ["le", "chat", "dort"]
print(" ".join(mots))            # "le chat dort"
print("-".join(mots))            # "le-chat-dort"
```

Retiens la syntaxe de `join` : c'est **le séparateur** qui appelle la méthode.

---

## Les méthodes de test (renvoient `True` / `False`)

```python
"bonjour".startswith("bon")   # True
"fichier.txt".endswith(".txt")# True
"42".isdigit()                # True   uniquement des chiffres ?
"abc".isalpha()               # True   uniquement des lettres ?
"Bonjour".islower()           # False
"chat" in "le chat dort"      # True   (l'opérateur "in" marche aussi sur le texte)
```

> 💡 `.isdigit()` est très pratique pour vérifier qu'un `input()` est bien un nombre avant de faire `int()`.

---

## Mise en forme

```python
"lucas".capitalize()          # "Lucas"    première lettre en majuscule
"lucas martin".title()        # "Lucas Martin"  chaque mot
"abc".center(11, "*")         # "****abc****"
"5".zfill(3)                  # "005"      complète avec des zéros
```

---

## Les f-strings, en détail

```python
prix = 3.14159
nom = "Lucas"

print(f"{prix:.2f}")      # 3.14      2 décimales
print(f"{prix:10.2f}")    # "      3.14"  aligné à droite sur 10 caractères
print(f"{nom:>10}")       # "     Lucas"  aligné à droite
print(f"{nom:<10}|")      # "Lucas     |"  aligné à gauche
print(f"{nom:^10}|")      # "  Lucas   |"  centré
print(f"{1234567:,}")     # 1,234,567  séparateur de milliers
```

Super utile pour afficher des tableaux alignés.

---

## Les caractères spéciaux

```python
print("ligne 1\nligne 2")     # \n = retour à la ligne
print("colonne1\tcolonne2")   # \t = tabulation
print("Il a dit \"salut\"")   # \" = un vrai guillemet
print("C:\\Users\\Lucas")     # \\ = un vrai antislash
```

Sur plusieurs lignes, on peut aussi utiliser les triples guillemets :

```python
texte = """Première ligne
Deuxième ligne
Troisième ligne"""
```

---

## Concaténer et répéter

```python
print("bon" + "jour")    # bonjour
print("ab" * 3)          # ababab
print("-" * 40)          # une ligne de séparation
```

⚠️ On ne peut pas coller du texte et un nombre : `"age : " + 25` plante.
Il faut `"age : " + str(25)` — ou mieux, une f-string.

---

## ➡️ À toi de jouer

Ouvre `exercices.py` : les deux énoncés sont écrits en haut du fichier.
Écris ton code en dessous, puis compare avec `solution.py`.
