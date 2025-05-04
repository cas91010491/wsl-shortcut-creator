# Development Guide

## Branching Strategy

This project follows a protected branch model with two main branches:

- `master`: Production-ready code
  - Protected branch
  - Requires pull request reviews
  - Must be up to date before merging
  - Direct pushes are not allowed

- `develop`: Integration branch for features
  - Where feature branches are merged
  - Testing ground for new features
  - Should be stable but can contain work in progress

### Feature Development Workflow

1. Create a feature branch from `develop`:
   ```powershell
   git checkout -b feature/your-feature-name develop
   ```

2. Make your changes and commit them:
   ```powershell
   git add .
   git commit -m "Description of your changes"
   ```

3. Push your feature branch and create a pull request:
   ```powershell
   git push -u origin feature/your-feature-name
   ```

4. Create a pull request to merge into `develop`
5. After review and approval, merge into `develop`
6. Once features are tested in `develop`, create a pull request to `master`

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
