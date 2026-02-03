# Hello World

> Directive d'exemple pour démontrer le workflow 3-layers.

## Goal

Générer un message de bienvenue personnalisé et l'enregistrer dans un fichier JSON.

## Inputs

- [ ] Nom de l'utilisateur (passé en argument)
- [ ] Langue souhaitée (fr, en, es) - optionnel, défaut: fr

## Tools / Scripts

| Script | Purpose |
|--------|---------|
| `execution/hello_world.py` | Génère le message de bienvenue |

## Process

1. Vérifier que le nom est fourni
2. Exécuter le script avec les arguments appropriés :
   ```bash
   python execution/hello_world.py --name "Jean" --lang fr
   ```
3. Vérifier la sortie dans `.tmp/hello_output.json`

## Outputs

- **Fichier JSON** : `.tmp/hello_output.json`
  ```json
  {
    "success": true,
    "name": "Jean",
    "message": "Bonjour Jean ! Bienvenue dans le boilerplate Orizon.",
    "timestamp": "2025-01-15T10:30:00"
  }
  ```

## Edge Cases & Learnings

- **Nom vide** : Le script retourne une erreur avec exit code 1
- **Langue non supportée** : Fallback automatique vers français
- **Caractères spéciaux** : Les accents sont supportés (UTF-8)
