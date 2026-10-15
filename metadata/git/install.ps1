# This script is used to install the git hook in the repository,
# embedding the contents of pre-commit.ps1 into a single hook file.

# Set working directory to the location of this script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location -Path $scriptPath

# Get the root directory of the repository
$repoRootDir = git rev-parse --show-toplevel
$hooksDir = Join-Path $repoRootDir '.git\hooks'

# Read the contents of pre-commit.ps1
$ps1Content = Get-Content -Raw -Path (Join-Path $scriptPath 'pre-commit.ps1')

# Build the Git hook script content as a Bash script that calls PowerShell
$hookScript = @"
#!/bin/bash 
# This Git hook calls the embedded PowerShell code

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command '
$ps1Content
'
"@

# Write the hook script to the hooks directory with Unix-style line endings
# The `-replace` ensures that all `\r` characters (Windows line endings) are removed
$hookScript = $hookScript -replace "`r`n", "`n"

# Create the hooks directory if it does not exist
if (-not (Test-Path $hooksDir)) {
    New-Item -ItemType Directory -Path $hooksDir
}

# Define the full path for the Git hook
$hookPath = Join-Path $hooksDir 'pre-commit'
# Write the hook script to the hooks directory
Set-Content -Path $hookPath -Value $hookScript
