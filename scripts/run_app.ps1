# Run WSL Shortcut Creator
param(
    [string]$VenvPath = ".venv"
)

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

Write-Host "Starting WSL Shortcut Creator..."
python -m wsl_shortcut_creator

# Deactivate virtual environment
deactivate
