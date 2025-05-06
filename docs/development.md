# Development Guide

## Setting Up Development Environment

1. Create the development environment and install all dependencies:
   ```powershell
   .\scripts\build.ps1
   ```
   This will:
   - Create a Python virtual environment (`.venv` by default)
   - Install all required dependencies
   - Install development dependencies
   - Install the package in development mode

2. To clean and rebuild the environment:
   ```powershell
   .\scripts\build.ps1 -Clean
   ```

3. Run tests:
   ```powershell
   .\scripts\run_tests.ps1
   ```

4. Run tests with coverage:
   ```powershell
   .\scripts\run_tests.ps1 -Coverage
   ```

Note: All commands will automatically use the virtual environment created by the build script.

## Project Structure

- `src/wsl_shortcut_creator/`: Main package directory
  - `__main__.py`: Application entry point
  - `config/`: Configuration management
  - `gui/`: GUI components
- `tests/`: Test files
- `docs/`: Documentation
- `scripts/`: Build and utility scripts

## Adding New Features

1. Create tests in the appropriate test file
2. Implement the feature
3. Run tests to verify functionality
4. Update documentation if needed

## Code Style

This project follows:
- PEP 8 style guide
- Type hints for all function parameters and returns
- Docstrings for all modules, classes, and functions

## Running Style Checks

These commands will run using the virtual environment:

```powershell
# Activate the virtual environment first (if not already activated)
. .\.venv\Scripts\Activate.ps1

# Run style checks
python -m pylint src/wsl_shortcut_creator
python -m black src/wsl_shortcut_creator
python -m mypy src/wsl_shortcut_creator

# Deactivate when done (optional)
deactivate
```

Note: The build script installs all necessary development tools in the virtual environment.
