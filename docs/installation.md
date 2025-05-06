# Installation Guide

## Requirements
- Windows 10 or later
- WSL (Windows Subsystem for Linux) installed and configured
- Python 3.8 or later

## Installation Steps
1. Clone the repository
2. Run the build script to set up the virtual environment and install dependencies:
   ```powershell
   .\scripts\build.ps1
   ```
3. Run the application:
   ```powershell
   .\scripts\run_app.ps1
   ```

The build script will:
- Create a Python virtual environment (`.venv` by default)
- Install all required dependencies
- Install the package in development mode

To clean and rebuild:
```powershell
.\scripts\build.ps1 -Clean
```

For a release build (without dev dependencies):
```powershell
.\scripts\build.ps1 -Release
```
