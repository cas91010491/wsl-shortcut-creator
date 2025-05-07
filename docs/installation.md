# Installation Guide

## Requirements
- Windows 10 or later
- WSL (Windows Subsystem for Linux) installed and configured
- Python 3.8 or later

## PowerShell Execution Policy
By default, Windows PowerShell's execution policy is set to "Restricted" for security reasons. You'll need to adjust this to run the build scripts. You have two options:

1. **Temporary Solution (Recommended)**
   This will allow script execution only for the current PowerShell session:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

2. **Permanent Solution**
   This will allow signed scripts to run for your user account:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

For more information about PowerShell execution policies, see [Microsoft's documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy).

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
