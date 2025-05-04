# -*- coding: utf-8 -*-
"""
WSL Shortcut Creator - Main Application Entry Point

This module serves as the entry point for the WSL Shortcut Creator application.
It initializes the GUI and sets up the main application window.

The application allows users to:
- Automatically detect GUI applications installed in WSL
- Create Windows shortcuts for WSL applications
- Manage existing shortcuts
- Configure application settings

Example:
    To run the application directly:
    
    ```python
    python main.py
    ```
    
    Or after installation:
    
    ```bash
    wsl-shortcuts
    ```

Dependencies:
    - PyQt5: GUI framework
    - utils.config_manager: Configuration management
    - gui.main_window: Main application window
"""

import os
import sys
import logging

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import application dependencies
try:
    from wsl_shortcut_creator.gui.main_window import MainWindow
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QIcon
except ImportError as e:
    logger.error(f"Failed to import required module: {e}")
    sys.exit(1)

def main():
    """Main entry point for the application."""
    try:
        # Create Qt application
        app = QApplication(sys.argv)
        app.setApplicationName("WSL Shortcut Creator")
        
        # Set application icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'images', 'Logo.ico')
        if os.path.exists(icon_path):
            app.setWindowIcon(QIcon(icon_path))
        else:
            logger.warning(f"Application icon not found at {icon_path}")
        
        # Create and show main window
        window = MainWindow()
        window.show()
        
        # Start event loop
        return_code = app.exec_()
        logger.info("Application exiting normally")
        return return_code
        
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
