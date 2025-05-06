# Test execution script for WSL Shortcut Creator
param(
    [switch]$Coverage,
    [switch]$Verbose,
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
