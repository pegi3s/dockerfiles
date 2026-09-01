#!/usr/bin/env powershell

# Initialize a variable to track errors
$errorOccurred = $false

$repoRoot = Get-Location  # Git hooks run in the repository root
$metadataPath = Join-Path $repoRoot "metadata"  # Metadata subdirectory

# Get all JSON files in the directory and its subdirectories
$jsonFiles = Get-ChildItem -Path $metadataPath -Recurse -Filter *.json

foreach ($file in $jsonFiles) {
    try {
        # Try to read and convert the JSON file to a PSObject or Hashtable object
        # This will throw an error if the JSON is not valid
        $jsonContent = Get-Content -Path $file.FullName -Raw | ConvertFrom-Json
    } catch {
        Write-Host "$($file.Name) has syntax errors."
        $errorOccurred = $true
    }
}

# Set the exit code based on whether any errors occurred
if ($errorOccurred) {
    exit 1  # Exit with a non-zero code to indicate failure
} else {
    exit 0  # Exit with zero code to indicate success
}
