# Orizon AI Coding Boilerplate

Une architecture de démarrage robuste et déterministe pour projets d'automatisation et de traitement de données pilotés par l'IA.

## 🏗️ Architecture 3-Layers

Ce projet utilise une séparation stricte des préoccupations pour maximiser la fiabilité :

1.  **Directive (Layer 1)** : SOPs en Markdown (`directives/`). Définit le **quoi** (instructions métier).
2.  **Orchestration (Layer 2)** : L'Agent IA (Moi). Je fais le routage intelligent entre les directives et les scripts.
3.  **Execution (Layer 3)** : Scripts Python déterministes (`execution/`). Effectue le travail concret (APIs, scraping, calculs).

## 🚀 Démarrage Rapide

### 1. Installation
```bash
# Cloner le dépôt
git clone <votre-repo-url>
cd orizon-ai-coding-boilerplate
```

### 2. Configuration
Copiez le fichier d'exemple et remplissez vos clés API :
```bash
cp .env.example .env
```

### 3. Utilisation
- Placez vos instructions dans `directives/`.
- Créez vos scripts de travail dans `execution/`.
- Les fichiers temporaires vont dans `.tmp/`.

## 🛠️ Outils Inclus
- **CI/CD** : Linting automatique via GitHub Actions.
- **Modèles** : Gabarits pour directives et scripts prêts à l'emploi.
- **Sécurité** : `.gitignore` configuré pour protéger vos secrets.

## 📄 Licences & Instructions
Voir [CLAUDE.md](CLAUDE.md) / [GEMINI.md](GEMINI.md) pour les principes opérationnels de l'agent.
