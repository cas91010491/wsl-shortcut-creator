# Development Guide

## Setting Up Development Environment

1. Install development dependencies:
   ```powershell
   pip install -r requirements-dev.txt
   ```

2. Run tests:
   ```powershell
   .\scripts\run_tests.ps1
   ```

3. Run tests with coverage:
   ```powershell
   .\scripts\run_tests.ps1 -Coverage
   ```

## Project Structure

- `src/wsl_shortcut_creator/`: Main package directory
  - `__main__.py`: Application entry point
  - `config/`: Configuration management
  - `gui/`: GUI components
  - `utils/`: Utility functions
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

```powershell
python -m pylint src/wsl_shortcut_creator
python -m black src/wsl_shortcut_creator
python -m mypy src/wsl_shortcut_creator
```
