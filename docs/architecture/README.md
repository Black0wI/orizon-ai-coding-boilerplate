# Architecture 3-Layers

Cette architecture sépare les préoccupations pour maximiser la fiabilité des systèmes pilotés par IA.

## Vue d'ensemble

```mermaid
flowchart TB
    subgraph L1["🎯 Layer 1: Directive"]
        D1[directives/*.md]
        D2[SOPs en Markdown]
        D3[Le QUOI faire]
    end

    subgraph L2["🧠 Layer 2: Orchestration"]
        O1[Agent IA]
        O2[Routage intelligent]
        O3[Décisions & Coordination]
    end

    subgraph L3["⚙️ Layer 3: Execution"]
        E1[execution/*.py]
        E2[Scripts déterministes]
        E3[Le COMMENT faire]
    end

    L1 --> L2
    L2 --> L3
    L3 -.->|Résultats & Logs| L2
    L2 -.->|Mise à jour| L1

    style L1 fill:#e1f5fe,stroke:#01579b
    style L2 fill:#fff3e0,stroke:#e65100
    style L3 fill:#e8f5e9,stroke:#2e7d32
```

## Flux de données

```mermaid
sequenceDiagram
    participant U as 👤 Utilisateur
    participant A as 🧠 Agent IA
    participant D as 📋 Directive
    participant S as ⚙️ Script
    participant O as 📦 Output

    U->>A: Demande
    A->>D: Lit les instructions
    D-->>A: SOP (étapes, outils)
    A->>S: Exécute avec arguments
    S->>O: Écrit résultats (.tmp/, Cloud)
    S-->>A: Exit code + logs
    alt Succès
        A-->>U: ✅ Résumé
    else Erreur
        A->>D: 🔄 Met à jour (self-anneal)
        A->>S: Corrige et réessaie
    end
```

## Rôle de chaque couche

| Layer | Responsabilité | Fichiers | Langage |
|-------|---------------|----------|---------|
| **Directive** | Définir les objectifs, inputs, outputs, edge cases | `directives/*.md` | Markdown |
| **Orchestration** | Lire les directives, décider, appeler les scripts | Agent IA (Claude, Gemini) | - |
| **Execution** | Effectuer le travail concret (APIs, calculs, I/O) | `execution/*.*` | Python, JS, Go, etc. |

## Pourquoi cette architecture ?

### Problème
Les LLMs sont **probabilistes** (90% de précision par étape). Sur 5 étapes :
```
0.90 × 0.90 × 0.90 × 0.90 × 0.90 = 59% de succès 😰
```

### Solution
Pousser la complexité vers le **code déterministe** :
- Scripts testables avec 100% de précision
- L'agent ne fait que le routage (décisions simples)
- Self-annealing : le système apprend de ses erreurs

## Bonnes pratiques

### Directives
- Écrire comme pour un employé mid-level
- Toujours référencer les scripts à utiliser
- Documenter les edge cases découverts

### Scripts
- Un script = une responsabilité
- Retourner des exit codes explicites
- Écrire les logs vers stderr, les données vers stdout/.tmp

### Self-Annealing
Quand une erreur survient :
1. Lire le message d'erreur
2. Corriger le script
3. Tester à nouveau
4. **Mettre à jour la directive** avec les learnings
