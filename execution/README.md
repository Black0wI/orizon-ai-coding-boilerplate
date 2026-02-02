# Execution Scripts

Deterministic Python scripts that do the actual work. The orchestration layer (AI agent) calls these scripts based on directives.

## Principles

1. **Deterministic**: Same inputs → same outputs
2. **Single responsibility**: Each script does one thing well
3. **Well-documented**: Clear docstrings and comments
4. **Error handling**: Graceful failures with actionable messages
5. **Testable**: Can be run standalone for debugging

## Script Template

```python
#!/usr/bin/env python3
"""
Script: example_script.py
Purpose: Brief description of what this script does

Usage:
    python execution/example_script.py --input file.json --output results.json

Inputs:
    - input: Path to input file
    
Outputs:
    - Writes results to specified output path
    
Environment Variables:
    - API_KEY: Required for authentication
"""

import argparse
import os
import json
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Example script')
    parser.add_argument('--input', required=True, help='Input file path')
    parser.add_argument('--output', required=True, help='Output file path')
    args = parser.parse_args()
    
    # Your logic here
    pass

if __name__ == '__main__':
    main()
```

## Conventions

| Convention | Example |
|------------|---------|
| Naming | `verb_noun.py` (e.g., `scrape_website.py`) |
| Config | Use `.env` via `python-dotenv` |
| Logging | Use `print()` or `logging` module |
| Temp files | Write to `.tmp/` |
| Exit codes | 0 = success, 1 = error |

## Dependencies

Add required packages to `requirements.txt` in the project root.
