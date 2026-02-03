# Guide de Contribution

Merci de votre intérêt pour contribuer au boilerplate Orizon AI Coding ! 🎉

## 🚀 Démarrage rapide

### 1. Fork et Clone
```bash
git clone https://github.com/<votre-username>/orizon-ai-coding-boilerplate.git
cd orizon-ai-coding-boilerplate
```

### 2. Configuration
```bash
make setup  # Installe pre-commit hooks et crée .env
```

### 3. Créer une branche
```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

## 📋 Types de contributions

### Directives
Nouvelles SOPs dans `directives/` :
1. Copiez `directives/_template.md`
2. Remplissez toutes les sections
3. Testez le workflow complet

### Scripts d'exécution
Nouveaux scripts dans `execution/` :
1. Copiez `execution/_template.py`
2. Suivez les conventions (argparse, exit codes, etc.)
3. Documentez les dépendances dans `requirements.txt`

### Documentation
- Améliorations du README
- Nouveaux guides dans `docs/`
- Corrections et clarifications

## ✅ Checklist avant PR

- [ ] Code testé localement
- [ ] Pre-commit hooks passent (`git commit` les exécute automatiquement)
- [ ] Documentation mise à jour si nécessaire
- [ ] Pas de secrets ou clés API dans le code
- [ ] Messages de commit clairs et descriptifs

## 📝 Convention de commits

Utilisez des messages descriptifs en français ou anglais :

```
feat: ajoute script de scraping LinkedIn
fix: corrige gestion des rate limits
docs: améliore documentation architecture
refactor: simplifie validation des inputs
```

## 🔄 Processus de Pull Request

1. **Créez votre PR** vers la branche `main`
2. **Décrivez** ce que fait votre PR et pourquoi
3. **Attendez** une review (généralement 24-48h)
4. **Adressez** les commentaires si nécessaire
5. **Merge** ! 🎉

## 🐛 Signaler un bug

Ouvrez une Issue GitHub avec :
- Description du comportement attendu vs actual
- Étapes pour reproduire
- Version Python et OS utilisés
- Logs pertinents (sans secrets !)

## 💡 Proposer une fonctionnalité

Ouvrez une Issue avec le label `enhancement` :
- Décrivez le cas d'usage
- Expliquez la valeur ajoutée
- Proposez une approche si vous en avez une

## 📖 Ressources

- [Architecture 3-Layers](docs/architecture/README.md)
- [Template de directive](directives/_template.md)
- [Template de script](execution/_template.py)

---

**Questions ?** Ouvrez une Issue, nous serons ravis de vous aider ! 💬
