#!/usr/bin/env python3
"""
Example Python script for OpenClaw skill.
Replace with your actual implementation.
"""

import os
import sys
import json
import argparse
from typing import Optional


def check_requirements() -> bool:
    """Check if required environment variables are set."""
    api_key = os.getenv('REQUIRED_API_KEY')
    if not api_key:
        print("Error: REQUIRED_API_KEY environment variable not set", file=sys.stderr)
        print("Set it with: export REQUIRED_API_KEY=your_key_here", file=sys.stderr)
        return False
    return True


def do_something(arg1: str, arg2: Optional[str] = None) -> dict:
    """
    Main function that does the actual work.
    
    Args:
        arg1: First argument description
        arg2: Second argument description (optional)
    
    Returns:
        Dictionary with results
    """
    # Your implementation here
    return {
        "status": "success",
        "arg1": arg1,
        "arg2": arg2,
        "result": "Example result"
    }


def main():
    """Entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Example OpenClaw skill script"
    )
    parser.add_argument(
        'arg1',
        help='First required argument'
    )
    parser.add_argument(
        '--arg2',
        default=None,
        help='Optional second argument'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )
    
    args = parser.parse_args()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Run main logic
    try:
        result = do_something(args.arg1, args.arg2)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Status: {result['status']}")
            print(f"Result: {result['result']}")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
