# Test execution script for WSL Shortcut Creator
param(
    [switch]$Coverage,
    [switch]$Verbose
)

$TestArgs = @("tests")

if ($Coverage) {
    $TestArgs += "--cov=src/wsl_shortcut_creator"
    $TestArgs += "--cov-report=term-missing"
}

if ($Verbose) {
    $TestArgs += "-v"
}

python -m pytest $TestArgs
