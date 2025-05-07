# Build script for WSL Shortcut Creator
param(
    [switch]$Clean,
    [switch]$Release,
    [string]$VenvPath = ".venv"
)

# Check PowerShell execution policy
$executionPolicy = Get-ExecutionPolicy
if ($executionPolicy -eq "Restricted") {
    Write-Host "Error: PowerShell execution policy is set to Restricted." -ForegroundColor Red
    Write-Host @"
    
To run this script, you need to change the PowerShell execution policy.
You have two options:

1. Temporary Solution (recommended, affects only current session):
   Open PowerShell and run:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

2. Permanent Solution (affects your user account):
   Open PowerShell and run:
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

For more information, see docs/installation.md
"@
    exit 1
}

# Clean build artifacts if requested
if ($Clean) {
    Write-Host "Cleaning build artifacts..."
    Get-ChildItem -Path "src" -Filter "__pycache__" -Recurse | Remove-Item -Recurse -Force
    if (Test-Path "build") { Remove-Item "build" -Recurse -Force }
    if (Test-Path "dist") { Remove-Item "dist" -Recurse -Force }
    if (Test-Path $VenvPath) { 
        Write-Host "Removing existing virtual environment..."
        Remove-Item $VenvPath -Recurse -Force 
    }
}

# Create and activate virtual environment
Write-Host "Setting up Python virtual environment..."
if (-not (Test-Path $VenvPath)) {
    python -m venv $VenvPath
}

# Get the path to the virtual environment's activate script
$ActivatePath = Join-Path $VenvPath "Scripts\Activate.ps1"
if (-not (Test-Path $ActivatePath)) {
    throw "Virtual environment activation script not found at: $ActivatePath"
}

# Activate the virtual environment
. $ActivatePath

# Upgrade pip in the virtual environment
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..."
python -m pip install -r requirements.txt

# Install development dependencies if not a release build
if (-not $Release) {
    Write-Host "Installing development dependencies..."
    python -m pip install -r requirements-dev.txt
}

# Install package in development mode
Write-Host "Installing package in development mode..."
python -m pip install -e .

# Run tests if not a release build
if (-not $Release) {
    Write-Host "Running tests..."
    python -m pytest tests
}

# Deactivate virtual environment (optional since the script is ending)
deactivate
