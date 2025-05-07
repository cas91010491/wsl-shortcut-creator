# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-05-07

### Added
- PowerShell execution policy checks in all scripts
- User-friendly error messages for restricted execution policy
- Detailed documentation about PowerShell execution policy in installation guide

### Changed
- Updated build.ps1, run_app.ps1, and run_tests.ps1 to handle restricted execution policies
- Enhanced installation documentation with execution policy guidance
- Improved error handling in PowerShell scripts

### Developer Experience
- Better error messages for common setup issues
- Clearer guidance for PowerShell security settings
- More robust script execution handling

## [1.1.0] - 2025-05-06

### Added
- Virtual environment support for development setup
- Automated venv creation in build script
- Venv-aware run and test scripts

### Changed
- Updated build.ps1 to create and use virtual environment
- Modified run_app.ps1 to use virtual environment
- Modified run_tests.ps1 to use virtual environment
- Updated all documentation for virtual environment usage

### Developer Experience
- Improved isolation of development dependencies
- Cleaner development setup process
- Consistent environment across all developers

## [1.0.0] - Initial Release

### Added
- Initial release of WSL Shortcut Creator
- GUI for managing WSL application shortcuts
- Automatic detection of WSL applications
- Custom application support
- Material Design interface
