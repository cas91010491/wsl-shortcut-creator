from typing import Dict, Optional, TypedDict
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os
from PIL import Image
import logging

# Setup module logger
logger = logging.getLogger(__name__)


class AppInfo(TypedDict):
    """Type definition for application information dictionary"""

    name: str
    command: str
    icon: Optional[str]


class CustomAppDialog(QDialog):
    """
    Dialog for adding custom WSL applications.

    This dialog allows users to manually specify application details including:
    - Application name
    - Command to run
    - Optional icon file
    """

    def __init__(self, parent: Optional[QDialog] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Add Custom Application")
        self.setModal(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Set window icon
        icon_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "imgs", "Logo.ico"
        )
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            logger.debug(f"Set dialog icon from {icon_path}")

        self.setup_ui()

    def setup_ui(self) -> None:
        """Initialize and setup the dialog's UI components."""
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        # Application Name
        name_layout = QHBoxLayout()
        name_label = QLabel("Application Name:")
        name_label.setMinimumWidth(100)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter application name...")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_edit)
        layout.addLayout(name_layout)

        # Command
        cmd_layout = QHBoxLayout()
        cmd_label = QLabel("Command Path:")
        cmd_label.setMinimumWidth(100)
        self.cmd_edit = QLineEdit()
        self.cmd_edit.setPlaceholderText("Enter WSL command or path...")
        cmd_layout.addWidget(cmd_label)
        cmd_layout.addWidget(self.cmd_edit)
        layout.addLayout(cmd_layout)

        # Icon
        icon_layout = QHBoxLayout()
        icon_label = QLabel("Icon (optional):")
        icon_label.setMinimumWidth(100)
        self.icon_path_label = QLabel("No icon selected")
        self.browse_icon_button = QPushButton("Browse...")
        self.browse_icon_button.clicked.connect(self.browse_icon)
        icon_layout.addWidget(icon_label)
        icon_layout.addWidget(self.icon_path_label)
        icon_layout.addWidget(self.browse_icon_button)
        layout.addLayout(icon_layout)

        # Add some vertical spacing
        layout.addSpacing(20)

        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Add")
        self.ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        # Style buttons
        self.ok_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """
        )

        cancel_button.setStyleSheet(
            """
            QPushButton {
                background-color: #9E9E9E;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #757575;
            }
            QPushButton:pressed {
                background-color: #616161;
            }
        """
        )

        self.browse_icon_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FFC107;
                color: black;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FFA000;
            }
            QPushButton:pressed {
                background-color: #FF8F00;
            }
        """
        )

        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(self.ok_button)
        layout.addLayout(button_layout)
        # Set dialog layout
        self.setLayout(layout)

        # Set minimum size
        self.setMinimumWidth(400)

    def convert_to_ico(self, image_path):
        """Convert image to ICO format if needed"""
        try:
            if image_path.lower().endswith(".ico"):
                return image_path

            # Create icons directory if it doesn't exist
            icons_dir = os.path.expandvars("%LOCALAPPDATA%\\WSL Shortcuts\\icons")
            os.makedirs(icons_dir, exist_ok=True)

            # Generate output path
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            ico_path = os.path.join(icons_dir, f"{base_name}.ico")

            # Convert image to ICO
            with Image.open(image_path) as img:
                # Convert to RGBA if needed
                if img.mode != "RGBA":
                    img = img.convert("RGBA")

                # Resize to standard icon sizes
                icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
                img.save(ico_path, format="ICO", sizes=icon_sizes)

            return ico_path

        except Exception as e:
            print(f"Error converting image: {e}")
            return None

    def browse_icon(self) -> None:
        """Open a file dialog to select an icon file."""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Icon",
            "",
            "Image Files (*.ico *.png *.jpg *.jpeg);;All Files (*.*)",
        )
        if file_name:
            # Convert to ICO if needed
            ico_path = self.convert_to_ico(file_name)
            if ico_path:
                self.icon_path = ico_path
                self.icon_path_label.setText(file_name)  # Show original path to user
            else:
                self.icon_path = None
                self.icon_path_label.setText("Error converting image")

    def get_app_info(self) -> AppInfo:
        """
        Get the information entered for the custom application.

        Returns:
            A dictionary containing the application information:
            - name: The name of the application
            - command: The command to run the application
            - icon: Optional path to the icon file
        """
        return {
            "name": self.name_edit.text().strip(),
            "command": self.cmd_edit.text().strip(),
            "icon": self.icon_path,
        }
