"""Basic test for main window functionality."""
import pytest
from wsl_shortcut_creator.gui.main_window import MainWindow

def test_main_window_creation(app):
    """Test that the main window can be created."""
    window = MainWindow()
    assert window is not None
