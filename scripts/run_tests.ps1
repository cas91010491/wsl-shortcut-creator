# Test execution script for WSL Shortcut Creator
param(
    [switch]$Coverage,
    [switch]$Verbose,
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

# Verify virtual environment exists
if (-not (Test-Path $VenvPath)) {
    Write-Error "Virtual environment not found. Please run build.ps1 first."
    exit 1
}

# Get the path to the virtual environment's activate script
$ActivatePath = Join-Path $VenvPath "Scripts\Activate.ps1"
if (-not (Test-Path $ActivatePath)) {
    Write-Error "Virtual environment activation script not found."
    exit 1
}

# Activate the virtual environment
. $ActivatePath

$TestArgs = @("tests")

if ($Coverage) {
    $TestArgs += "--cov=src/wsl_shortcut_creator"
    $TestArgs += "--cov-report=term-missing"
}

if ($Verbose) {
    $TestArgs += "-v"
}

python -m pytest $TestArgs

# Deactivate virtual environment
deactivate
