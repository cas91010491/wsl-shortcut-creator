# Usage Guide

## Starting the Application

Run the application using:

```powershell
python -m wsl_shortcut_creator
```
or 

```powershell
.\scripts\run_app.ps1
```

## Main Features

### Detecting WSL Applications
1. The application automatically scans your WSL distribution for installed GUI applications
2. Found applications will appear in the left list

### Creating Shortcuts
1. Select one or more applications from the left list
2. Click "Create Shortcut" to create Windows shortcuts
3. Shortcuts will appear in your Start Menu under your WSL distribution name

### Adding Custom Applications
1. Click "Add Custom Application"
2. Enter:
   - Application Name: The name that will appear in the Start Menu
   - Command: The WSL command to run the application
   - Icon (optional): A custom icon for the shortcut

### Managing Shortcuts
1. Existing shortcuts appear in the right list
2. Select one or more shortcuts and click "Remove Selected" to delete them

## Troubleshooting

If no applications are found:
1. Ensure WSL is properly installed and configured
2. Install some GUI applications in your WSL distribution
3. Try restarting the application
