# Execution Layer

Deterministic scripts that perform the actual work (API calls, data processing, file operations, etc.). The orchestration layer (AI agent) calls these scripts based on directives.

## Principles

1.  **Deterministic**: Same inputs should always yield the same outputs.
2.  **Language Agnostic**: You can use Python, Node.js, Go, Rust, Bash, or any other language as long as it handles inputs/outputs consistently.
3.  **Single Responsibility**: Each script should do one thing well.
4.  **Error Handling**: Scripts must return non-zero exit codes on failure with clear error messages to allow the agent to self-anneal.
5.  **Testable**: Scripts should be runnable standalone for validation.

## Standard Interface

To ensure portability across languages, follow these conventions:

### Inputs
Pass inputs via command-line arguments (preferred) or environment variables.

### Outputs
- Write deliverables to external services (Cloud, APIs, etc.).
- Write intermediate files to `.tmp/`.

### Environment Variables
Use a `.env` file for secrets and configuration.

## Language Examples

### Python 🐍
```python
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    # Logic here
    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Node.js 🟩
```javascript
const fs = require('fs');
require('dotenv').config();

const input = process.argv.slice(2)[0];
// Logic here
process.exit(0);
```

### Bash 🐚
```bash
#!/bin/bash
set -e
source .env
# Logic here
```

## Dependencies
Document language-specific dependencies in the root (e.g., `package.json`, `go.mod`, `requirements.txt`).
