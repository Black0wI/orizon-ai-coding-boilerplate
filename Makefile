.PHONY: setup clean test help

help:
	@echo "Orizon AI Coding Boilerplate - Commandes disponibles:"
	@echo "  make setup    - Installe les hooks de pre-commit"
	@echo "  make clean    - Nettoie les fichiers temporaires (.tmp/)"
	@echo "  make test     - Lance les tests (à configurer selon le langage)"

setup:
	@echo "Configuration du projet..."
	pre-commit install
	@if [ ! -f .env ]; then cp .env.example .env && echo ".env créé à partir de .env.example"; fi

clean:
	@echo "Nettoyage de .tmp/..."
	rm -rf .tmp/*
	touch .tmp/.gitkeep

test:
	@echo "Lancement des tests..."
	@# Ajoutez ici votre commande de test spécifique (ex: pytest, npm test, go test)
	@echo "Aucune suite de tests configurée pour le moment."
