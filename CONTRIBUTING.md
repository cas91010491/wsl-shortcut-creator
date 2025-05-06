# Contributing to WSL Shortcut Creator

Thank you for your interest in contributing to WSL Shortcut Creator! This document provides guidelines and rules for development work on the project.

## Development Branch Rules

### Branch Structure
- `master`: Main production branch
- `develop`: Main development branch
- Feature branches: `feature/<feature-name>`
- Bug fix branches: `fix/<bug-name>`
- Release branches: `release/v<version>`

### Branch Workflow
1. All development work should be done in feature branches
2. Feature branches should be created from `develop`
3. When complete, feature branches are merged back into `develop`
4. Release branches are created from `develop` when ready
5. Release branches are merged into both `master` and `develop`

### Branch Naming Conventions
- Use lowercase letters and hyphens
- Be descriptive but concise
- Examples:
  - `feature/custom-icons`
  - `fix/wsl-path-detection`
  - `release/v1.1.0`

### Commit Guidelines
1. Write clear, descriptive commit messages
2. Use present tense ("Add feature" not "Added feature")
3. Reference issue numbers when applicable
4. Keep commits focused and atomic
5. Commit message format:
   ```
   <type>: <description>

   [optional body]
   [optional footer]
   ```
   Types: feat, fix, docs, style, refactor, test, chore

### Code Review Process
1. Create a Pull Request (PR) to merge into `develop`
2. Ensure all tests pass
3. Request review from at least one maintainer
4. Address review comments
5. Squash commits if requested

## Development Standards

### Code Quality
- Follow PEP 8 style guide
- Include type hints for all functions
- Write docstrings for all modules, classes, and functions
- Maintain test coverage (aim for 80%+)
- Run style checks before committing:
  ```powershell
  python -m pylint src/wsl_shortcut_creator
  python -m black src/wsl_shortcut_creator
  python -m mypy src/wsl_shortcut_creator
  ```

### Testing Requirements
- Write tests for all new features
- Update existing tests when modifying features
- Run the full test suite before creating PR:
  ```powershell
  .\scripts\run_tests.ps1 -Coverage
  ```

### Documentation
- Update relevant documentation when adding/changing features
- Include docstrings for all public APIs
- Update the changelog for significant changes

### Dependencies
- Any new dependencies must be:
  1. Clearly necessary
  2. Actively maintained
  3. Compatible with our license
  4. Added to the appropriate requirements file

## Release Process

### Version Numbering
- Follow Semantic Versioning (MAJOR.MINOR.PATCH)
- Update version in:
  - `src/wsl_shortcut_creator/__init__.py`
  - `pyproject.toml`

### Release Checklist
1. Create release branch from `develop`
2. Update version numbers
3. Update changelog
4. Run full test suite
5. Create PR to merge into `master`
6. After merge, tag the release
7. Merge back into `develop`

## Getting Help
- Review existing issues and documentation
- Ask questions in discussions
- Contact maintainers for clarification

## Code of Conduct
- Be respectful and inclusive
- Follow the project's code of conduct
- Report inappropriate behavior to maintainers
