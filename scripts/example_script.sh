#!/usr/bin/env bash
#
# Example script for OpenClaw skill
# Replace this with your actual script logic

set -euo pipefail

# Check for required environment variables
if [[ -z "${REQUIRED_API_KEY:-}" ]]; then
    echo "Error: REQUIRED_API_KEY environment variable not set"
    echo "Set it with: export REQUIRED_API_KEY=your_key_here"
    exit 1
fi

# Check for required binaries
for cmd in jq curl; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: Required command '$cmd' not found"
        echo "Install it with your package manager"
        exit 1
    fi
done

# Script arguments
ARG1="${1:-default_value}"
ARG2="${2:-}"

# Main logic
main() {
    echo "Running skill with ARG1=$ARG1"
    
    # Example API call
    response=$(curl -s -H "Authorization: Bearer ${REQUIRED_API_KEY}" \
        "https://api.example.com/endpoint?param=$ARG1")
    
    # Parse response
    result=$(echo "$response" | jq -r '.data')
    
    echo "Result: $result"
}

# Run main function
main "$@"
