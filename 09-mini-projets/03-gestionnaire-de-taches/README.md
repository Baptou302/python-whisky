# Mini-projet 03 — Le gestionnaire de tâches ⭐⭐⭐

## Objectif

Une to-do list en ligne de commande, qui **sauvegarde les tâches dans un fichier**
pour qu'on les retrouve à la prochaine ouverture du programme.

C'est le projet le plus complet : il combine tout ce que tu as appris.

## Exemple d'utilisation

```
=================================
   GESTIONNAIRE DE TÂCHES
=================================

--- MES TÂCHES ---
  1. [ ] Acheter du pain          (normale)
  2. [x] Appeler le dentiste      (haute)
  3. [ ] Réviser Python           (haute)

  1 tâche(s) terminée(s) sur 3

Que veux-tu faire ?
  1. Ajouter une tâche
  2. Marquer une tâche comme terminée
  3. Supprimer une tâche
  4. Quitter

Ton choix : 1

Titre de la tâche : Faire les courses
Priorité (basse/normale/haute) [normale] :

  ✅ Tâche ajoutée !
```

## Cahier des charges

### Version de base

- [ ] Afficher la liste des tâches avec leur statut (`[ ]` ou `[x]`)
- [ ] Ajouter une tâche
- [ ] Marquer une tâche comme terminée
- [ ] Supprimer une tâche
- [ ] Quitter proprement

### La persistance (le cœur du projet)

- [ ] **Charger** les tâches depuis `taches.json` au démarrage
- [ ] **Sauvegarder** dans `taches.json` après chaque modification
- [ ] Si le fichier n'existe pas (premier lancement) → partir d'une liste vide, sans planter

### Les cas particuliers à gérer

- [ ] Numéro de tâche invalide (0, 99, "abc") → message d'erreur, pas de plantage
- [ ] Liste vide → afficher "Aucune tâche" plutôt qu'un tableau vide
- [ ] Titre vide → refuser d'ajouter

### Bonus

- [ ] Une **priorité** (basse / normale / haute) affichée et triable
- [ ] Une **date de création** (`from datetime import datetime`)
- [ ] Filtrer : afficher seulement les tâches non terminées
- [ ] Modifier le titre d'une tâche existante

## La structure des données

C'est la décision la plus importante du projet. On utilise une **liste de dictionnaires** :

```python
taches = [
    {"titre": "Acheter du pain", "terminee": False, "priorite": "normale"},
    {"titre": "Appeler le dentiste", "terminee": True, "priorite": "haute"},
]
```

Cette structure se traduit **directement** en JSON, ce qui rend la sauvegarde triviale.

## Rappel JSON

```python
import json

# Sauvegarder
with open("taches.json", "w", encoding="utf-8") as f:
    json.dump(taches, f, indent=2, ensure_ascii=False)

# Charger
with open("taches.json", "r", encoding="utf-8") as f:
    taches = json.load(f)
```

## Structure conseillée

```python
def charger_taches():
    """Lit taches.json, ou renvoie [] si le fichier n'existe pas."""

def sauvegarder_taches(taches):
    """Écrit la liste dans taches.json."""

def afficher_taches(taches):
    """Affiche la liste formatée."""

def ajouter_tache(taches):
    """Demande les infos et ajoute une tâche."""

def terminer_tache(taches):
    """Demande un numéro et marque la tâche comme terminée."""

def supprimer_tache(taches):
    """Demande un numéro et supprime la tâche."""

def main():
    """Le menu principal."""
```

> ⚠️ **Attention aux numéros !** L'utilisateur voit "1, 2, 3" mais Python indexe "0, 1, 2".
> Il faut faire `-1` quand tu convertis un choix utilisateur en index.

## Notions utilisées

Tous les chapitres : conditions, boucles, fonctions, listes, dictionnaires, chaînes, fichiers.

## Lancer

```bash
python starter.py
python solution.py
```

Le fichier `taches.json` sera créé automatiquement à côté du script.
