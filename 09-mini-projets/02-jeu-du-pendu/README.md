# Mini-projet 02 — Le jeu du pendu ⭐⭐

## Objectif

L'ordinateur choisit un mot au hasard. Le joueur propose des lettres une par une.
À chaque erreur, le pendu se dessine un peu plus. 7 erreurs = perdu.

## Exemple d'utilisation

```
=========================
    LE JEU DU PENDU
=========================

Le mot contient 6 lettres.

  +---+
      |
      |
      |
     ===

Mot : _ _ _ _ _ _
Lettres déjà proposées : (aucune)
Erreurs : 0/7

Propose une lettre : e

  ✅ Bien vu ! Il y a des "e".

Mot : _ _ _ _ _ e
...
```

## Cahier des charges

### Version de base

- [ ] Choisir un mot au hasard dans une liste
- [ ] Afficher le mot masqué avec des `_`
- [ ] Demander une lettre au joueur
- [ ] Révéler les occurrences de cette lettre si elle est dans le mot
- [ ] Compter les erreurs
- [ ] Arrêter quand le mot est trouvé (gagné) ou à 7 erreurs (perdu)

### Les cas particuliers à gérer

- [ ] Le joueur propose **une lettre déjà proposée** → le prévenir, ne pas compter d'erreur
- [ ] Le joueur tape **plusieurs caractères** ou un chiffre → redemander
- [ ] Gérer les **majuscules** (si le joueur tape "A", ça doit marcher)

### Bonus

- [ ] Dessiner le **pendu en ASCII** qui se construit à chaque erreur
- [ ] Afficher la liste des **lettres déjà proposées**
- [ ] Ajouter des **niveaux de difficulté** (mots courts / longs)
- [ ] Proposer de **rejouer** à la fin

## Le module `random`

```python
import random

mots = ["python", "ordinateur", "clavier"]
mot = random.choice(mots)        # choisit un élément au hasard

random.randint(1, 6)             # un entier au hasard entre 1 et 6 (inclus)
random.shuffle(ma_liste)         # mélange une liste
```

## Structure conseillée

```python
def choisir_mot():
    """Renvoie un mot au hasard."""

def afficher_mot(mot, lettres_trouvees):
    """Renvoie le mot avec des _ pour les lettres non trouvées."""

def demander_lettre(lettres_proposees):
    """Demande une lettre valide et non déjà proposée."""

def dessiner_pendu(erreurs):
    """Affiche le dessin correspondant au nombre d'erreurs."""

def main():
    """La boucle de jeu."""
```

> 💡 **Astuce clé** : garde une liste `lettres_trouvees` des lettres devinées.
> Pour afficher le mot, parcours-le lettre par lettre : si la lettre est dans
> `lettres_trouvees`, affiche-la, sinon affiche `_`.

## Notions utilisées

Chapitres 03 (boucles), 04 (fonctions), 05 (listes), 07 (chaînes).

## Lancer

```bash
python starter.py
python solution.py
```
