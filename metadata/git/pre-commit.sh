#!/bin/bash

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed. Please install it to run this hook."
    exit 1
fi

# Exit on error
set -e

# Check all JSON files in the metadata directory
echo "Checking JSON syntax in metadata JSON files..."
INVALID_FILES=""

# Find all JSON files in the repository
JSON_FILES=$(find metadata -name "*.json" -type f)

# If no JSON files found, exit successfully
if [ -z "$JSON_FILES" ]; then
    echo "No JSON files found."
    exit 0
fi

# Check each JSON file
for file in $JSON_FILES; do
    echo "Checking $file..."
    if ! cat "$file" | jq type 1>/dev/null; then
        INVALID_FILES="$INVALID_FILES\n  - $file"
    fi
done

# If invalid files were found, exit with error
if [ -n "$INVALID_FILES" ]; then
    echo -e "\nError: The following JSON files have invalid syntax:$INVALID_FILES"
    echo "Please fix the JSON syntax before committing."
    exit 1
fi

echo "All JSON files are valid."
exit 0