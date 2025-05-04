# Build script for WSL Shortcut Creator
param(
    [switch]$Clean,
    [switch]$Release
)

# Clean build artifacts if requested
if ($Clean) {
    Write-Host "Cleaning build artifacts..."
    Get-ChildItem -Path "src" -Filter "__pycache__" -Recurse | Remove-Item -Recurse -Force
    if (Test-Path "build") { Remove-Item "build" -Recurse -Force }
    if (Test-Path "dist") { Remove-Item "dist" -Recurse -Force }
}

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
