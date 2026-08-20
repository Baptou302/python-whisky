# Mini-projet 01 — La calculatrice ⭐

## Objectif

Un programme qui demande deux nombres et une opération, affiche le résultat,
et recommence tant que l'utilisateur le souhaite.

## Exemple d'utilisation

```
=========================
   CALCULATRICE
=========================

Premier nombre : 12
Opération (+ - * /) : *
Deuxième nombre : 4

  12.0 * 4.0 = 48.0

Continuer ? (o/n) : o

Premier nombre : 10
Opération (+ - * /) : /
Deuxième nombre : 0

  Erreur : division par zéro impossible.

Continuer ? (o/n) : n

À bientôt !
```

## Cahier des charges

### Version de base

- [ ] Demander un premier nombre
- [ ] Demander une opération (`+`, `-`, `*`, `/`)
- [ ] Demander un deuxième nombre
- [ ] Afficher le résultat
- [ ] Demander si on continue, et recommencer si oui

### Les cas particuliers à gérer

- [ ] **Division par zéro** → afficher un message d'erreur au lieu de planter
- [ ] **Saisie invalide** (l'utilisateur tape "abc" au lieu d'un nombre) → redemander
- [ ] **Opération inconnue** → redemander

### Bonus (si tu veux aller plus loin)

- [ ] Ajouter les opérations `%` (modulo) et `**` (puissance)
- [ ] Garder un **historique** des calculs et l'afficher à la fin
- [ ] Ajouter une commande "memoire" qui réutilise le dernier résultat

## Structure conseillée

Découpe en petites fonctions, chacune faisant **une seule chose** :

```python
def demander_nombre(message):
    """Demande un nombre à l'utilisateur, redemande tant que ce n'est pas valide."""

def demander_operation():
    """Demande une opération valide."""

def calculer(a, operation, b):
    """Renvoie le résultat, ou None si l'opération est impossible."""

def main():
    """La boucle principale du programme."""
```

## Notions utilisées

Chapitres 01 (variables, input), 02 (conditions), 03 (boucle while), 04 (fonctions).

## Lancer

```bash
python starter.py     # ta version
python solution.py    # la correction
```
