#!/usr/bin/env python3
"""
Hello World Script

Generates a personalized welcome message in the specified language.
This is an example script demonstrating the execution layer conventions.

Usage:
    python execution/hello_world.py --name <name> [--lang <fr|en|es>] [--output <path>]

Example:
    python execution/hello_world.py --name "Marie" --lang fr
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Supported languages and their welcome messages
MESSAGES = {
    "fr": "Bonjour {name} ! Bienvenue dans le boilerplate Orizon.",
    "en": "Hello {name}! Welcome to the Orizon boilerplate.",
    "es": "¡Hola {name}! Bienvenido al boilerplate Orizon.",
}

DEFAULT_LANG = "fr"
DEFAULT_OUTPUT = ".tmp/hello_output.json"


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a personalized welcome message",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Name of the person to greet",
    )
    parser.add_argument(
        "--lang",
        choices=list(MESSAGES.keys()),
        default=DEFAULT_LANG,
        help=f"Language for the message (default: {DEFAULT_LANG})",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Path to output file (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    return parser.parse_args()


def generate_message(name: str, lang: str) -> str:
    """
    Generate a welcome message for the given name and language.

    Args:
        name: The name to include in the message
        lang: Language code (fr, en, es)

    Returns:
        Formatted welcome message
    """
    # Fallback to default language if not supported
    if lang not in MESSAGES:
        print(f"⚠️  Language '{lang}' not supported, falling back to '{DEFAULT_LANG}'", file=sys.stderr)
        lang = DEFAULT_LANG

    return MESSAGES[lang].format(name=name)


def main():
    """Main entry point."""
    args = parse_args()

    # Validate name
    if not args.name.strip():
        print("❌ Error: Name cannot be empty", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"📥 Name: {args.name}")
        print(f"🌐 Language: {args.lang}")

    # Generate message
    message = generate_message(args.name.strip(), args.lang)

    # Build result
    result = {
        "success": True,
        "name": args.name.strip(),
        "lang": args.lang,
        "message": message,
        "timestamp": datetime.now().isoformat(),
    }

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    if args.verbose:
        print(f"✅ Output written to {output_path}")

    # Print result to stdout for easy piping
    print(json.dumps(result, indent=2, ensure_ascii=False))

    sys.exit(0)


if __name__ == "__main__":
    main()
