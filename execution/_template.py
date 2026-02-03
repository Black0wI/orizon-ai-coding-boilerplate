#!/usr/bin/env python3
"""
[Script Name]

Brief description of what this script does.

Usage:
    python execution/_template.py --input <value> [--output <path>]

Example:
    python execution/_template.py --input "Hello World" --output .tmp/result.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Load environment variables from .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, rely on system env vars


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="[Script description]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input value or path to input file",
    )
    parser.add_argument(
        "--output",
        default=".tmp/output.json",
        help="Path to output file (default: .tmp/output.json)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    return parser.parse_args()


def validate_environment():
    """
    Validate that required environment variables are set.
    Returns tuple of (success: bool, missing: list).
    """
    required_vars = [
        # "API_KEY",  # Uncomment and add required vars
    ]
    missing = [var for var in required_vars if not os.getenv(var)]
    return len(missing) == 0, missing


def main():
    """Main entry point."""
    args = parse_args()

    # Validate environment
    valid, missing = validate_environment()
    if not valid:
        print(f"❌ Error: Missing required environment variables: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"📥 Input: {args.input}")
        print(f"📤 Output: {args.output}")

    # ========================================
    # YOUR LOGIC HERE
    # ========================================
    try:
        result = {
            "success": True,
            "input": args.input,
            "message": "Template script executed successfully",
        }
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    # ========================================

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    if args.verbose:
        print(f"✅ Output written to {output_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()
