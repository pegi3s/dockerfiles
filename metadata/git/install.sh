#!/bin/bash

# This script is used to install the git hooks in the repository.

# Set working directory to the location of this script
cd "$(dirname "${BASH_SOURCE[0]}")"

# Check if the necessary programs to run the hooks are installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed. Please install it to run this hook."
    exit 1
fi

# Get the root directory of the repository
REPO_ROOT_DIR=$(git rev-parse --show-toplevel)
HOOKS_DIR="$REPO_ROOT_DIR/.git/hooks"

# Create the hooks directory if it does not exist
if [ ! -d "$HOOKS_DIR" ]; then
    mkdir -p "$HOOKS_DIR"
fi

# Move the hooks to the hooks directory
cp pre-commit.sh "$HOOKS_DIR/pre-commit"
