"""Test configuration and fixtures."""
import pytest
from PyQt5.QtWidgets import QApplication
import sys

@pytest.fixture(scope="session")
def app():
    """Create a Qt application instance for tests."""
    return QApplication(sys.argv)
