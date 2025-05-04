"""Main window for the WSL Shortcut Creator application."""
from typing import Dict, Optional, Union, TypedDict

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QAbstractItemView
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

import os
import logging
import subprocess

from .ui_constants import COLORS, STYLES
from .custom_app_dialog import AppInfo, CustomAppDialog

# Setup module logger
logger = logging.getLogger(__name__)

class WSLDistroInfo(TypedDict):
    """Type definition for WSL distribution information"""
    name: Optional[str]
    folder: Optional[str]

# Setup module logger
logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    """
    Main window for the WSL Shortcut Creator application.
    
    This window allows users to:
    - View and select WSL applications
    - Create Windows shortcuts for selected applications
    - Manage existing shortcuts
    - Add custom applications
    """

    def __init__(self) -> None:
        """Initialize the main window and set up the UI components."""
        super().__init__()
        
        # Initialize instance variables
        self.distro_name, self.folder_name = self.get_wsl_distro_info()
        if not self.distro_name:
            logger.error("No WSL distribution found")
            
        # Set up window properties
        self.setWindowTitle("WSL Shortcut Creator")
        self.setMinimumSize(800, 600)
        
        # Set window icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'resources', 'images', 'Logo.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            logger.debug(f"Set window icon from {icon_path}")
        
        # Initialize UI
        self.init_ui()
        self.load_existing_shortcuts()
        self.load_wsl_applications()
    

    def init_ui(self) -> None:
        """Initialize and set up the UI components."""
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Create lists layout
        lists_layout = QHBoxLayout()
        
        # WSL Applications section
        app_layout = QVBoxLayout()
        app_label = QLabel("Available WSL Applications")
        app_label.setStyleSheet(STYLES['label'])
        self.app_listbox = QListWidget()
        self.app_listbox.setStyleSheet(STYLES['list'])
        self.app_listbox.setSelectionMode(QAbstractItemView.ExtendedSelection)
        app_layout.addWidget(app_label)
        app_layout.addWidget(self.app_listbox)
        
        # Add custom app button
        self.add_custom_btn = QPushButton("Add Custom Application")
        self.add_custom_btn.setStyleSheet(STYLES['button'])
        self.add_custom_btn.clicked.connect(self.add_custom_application)
        app_layout.addWidget(self.add_custom_btn)
        
        lists_layout.addLayout(app_layout)
        
        # Action buttons
        action_layout = QVBoxLayout()
        action_layout.addStretch()
        
        self.create_shortcut_btn = QPushButton("Create Shortcut >>")
        self.create_shortcut_btn.setStyleSheet(STYLES['button'])
        self.create_shortcut_btn.clicked.connect(self.create_shortcut)
        action_layout.addWidget(self.create_shortcut_btn)
        
        action_layout.addStretch()
        lists_layout.addLayout(action_layout)
        
        # Shortcuts section
        shortcut_layout = QVBoxLayout()
        shortcut_label = QLabel("Existing Shortcuts")
        shortcut_label.setStyleSheet(STYLES['label'])
        self.shortcuts_listbox = QListWidget()
        self.shortcuts_listbox.setStyleSheet(STYLES['list'])
        # Use explicit value for ExtendedSelection (3)
        self.shortcuts_listbox.setSelectionMode(3)  # type: ignore
        shortcut_layout.addWidget(shortcut_label)
        shortcut_layout.addWidget(self.shortcuts_listbox)
        
        # Remove shortcut button
        self.remove_shortcut_btn = QPushButton("Remove Selected")
        self.remove_shortcut_btn.setStyleSheet(STYLES['danger_button'])
        self.remove_shortcut_btn.clicked.connect(self.remove_shortcut)
        shortcut_layout.addWidget(self.remove_shortcut_btn)
        
        lists_layout.addLayout(shortcut_layout)
        
        layout.addLayout(lists_layout)
        
        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet(STYLES['status_label'])
        layout.addWidget(self.status_label)
    
    def update_status(self, message: str, is_error: bool = False) -> None:
        """
        Update the status label with a message.
        
        Args:
            message: The message to display
            is_error: Whether this is an error message
        """
        self.status_label.setText(message)
        if is_error:
            self.status_label.setStyleSheet(f"""
                QLabel {{
                    color: white;
                    background-color: {COLORS['danger']};
                    padding: 8px;
                    border-radius: 4px;
                    font-weight: bold;
                }}
            """)
            logger.error(message)
        else:
            # Show success state temporarily for non-error messages
            self.status_label.setStyleSheet(f"""
                QLabel {{
                    color: white;
                    background-color: {COLORS['success']};
                    padding: 8px;
                    border-radius: 4px;
                    font-weight: bold;
                }}
            """)
            # Reset to normal style after 3 seconds
            QTimer.singleShot(3000, lambda: self.status_label.setStyleSheet(STYLES['status_label']))
            logger.info(message)

    def load_existing_shortcuts(self) -> None:
        """
        Load existing shortcuts from the WSL default location.
        
        This method scans the Windows Start Menu directory for the current WSL
        distribution and populates the shortcuts listbox with any .lnk files found.
        """
        try:
            if not self.folder_name:
                self.update_status("No WSL distribution detected", True)
                logger.warning("No folder name available")
                return
                
            # Clean up the folder name and normalize it for Windows paths
            folder_name = self.folder_name
            start_menu = os.path.expandvars(
                os.path.join('%AppData%', 'Microsoft', 'Windows', 'Start Menu', 'Programs', folder_name)
            )
            logger.debug(f"Looking for shortcuts in: {start_menu}")
            
            # Clear existing items before adding new ones
            self.shortcuts_listbox.clear()
            
            if os.path.exists(start_menu):
                shortcuts = [f for f in os.listdir(start_menu) if f.endswith('.lnk')]
                logger.debug(f"Found shortcuts: {shortcuts}")
                
                for shortcut in shortcuts:
                    self.shortcuts_listbox.addItem(shortcut)
                    logger.debug(f"Added shortcut to list: {shortcut}")
                
                self.update_status(
                    "No shortcuts found" if not shortcuts 
                    else f"Found {len(shortcuts)} shortcut{'s' if len(shortcuts) != 1 else ''}"
                )
            else:
                logger.info(f"WSL shortcuts folder not found at: {start_menu}")
                try:
                    os.makedirs(start_menu)
                    logger.info(f"Created shortcuts directory: {start_menu}")
                    self.update_status("Created shortcuts folder - ready to add shortcuts")
                except Exception as e:
                    logger.error(f"Error creating directory: {e}")
                    self.update_status(f"Could not create shortcuts folder: {e}", True)
                
        except Exception as e:
            error_msg = f"Error loading shortcuts: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.update_status(error_msg, True)

    def remove_shortcut(self) -> None:
        """
        Remove the selected shortcut(s) from both the list and the file system.
        
        This method handles both single and multiple shortcut removal.
        """
        selected_items = self.shortcuts_listbox.selectedItems()
        if not selected_items:
            self.update_status("Please select a shortcut to remove", True)
            return
        
        try:
            removed_count = 0
            for item in selected_items:
                shortcut_name = item.text()
                # Clean up the folder name and create the shortcut path
                folder_name = self.folder_name
                shortcut_path = os.path.expandvars(
                    os.path.join('%AppData%', 'Microsoft', 'Windows', 'Start Menu', 'Programs', folder_name, shortcut_name)
                )
                if os.path.exists(shortcut_path):
                    try:
                        os.remove(shortcut_path)
                        self.shortcuts_listbox.takeItem(self.shortcuts_listbox.row(item))
                        removed_count += 1
                        logger.debug(f"Removed shortcut: {shortcut_path}")
                    except Exception as e:
                        logger.error(f"Failed to remove shortcut {shortcut_name}: {e}")
                        self.update_status(f"Error removing {shortcut_name}: {e}", True)
                        continue
            
            if removed_count > 0:
                self.update_status(
                    f"Successfully removed {removed_count} shortcut{'s' if removed_count != 1 else ''}"
                )
                # Update status with success styling
                self.status_label.setStyleSheet("""
                    QLabel {
                        color: white;
                        background-color: """ + COLORS['success'] + """;
                        padding: 8px;
                        border-radius: 4px;
                        font-weight: bold;
                    }
                """)
                # Reset the style after 3 seconds
                QTimer.singleShot(3000, lambda: self.status_label.setStyleSheet(STYLES['status_label']))
                
        except Exception as e:
            error_msg = f"Error removing shortcuts: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.update_status(error_msg, True)

    def load_wsl_applications(self) -> None:
        """
        Load WSL applications by scanning common installation directories.
        
        This method searches for .desktop files in standard Linux application directories
        and extracts application names from them.
        """
        try:
            self.update_status("Scanning for WSL applications...")
            self.app_listbox.clear()
            
            search_paths = [
                '/usr/share/applications/*.desktop',
                '/var/lib/snapd/desktop/applications/*.desktop',
                '~/.local/share/applications/*.desktop'
            ]
            
            apps_found = 0
            for search_path in search_paths:
                cmd = f'wsl -- ls {search_path}'
                logger.debug(f"Executing command: {cmd}")
                result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                
                if result.returncode == 0 and result.stdout.strip():
                    desktop_files = result.stdout.strip().split('\n')
                    for file_path in desktop_files:
                        if not file_path:  # Skip empty lines
                            continue
                        
                        # Read application name from .desktop file
                        name_cmd = ['wsl', '--', '/bin/bash', '-c', 
                                  f'cat "{file_path}" | grep "^Name=" | head -n 1']
                        name_result = subprocess.run(name_cmd, capture_output=True, text=True)
                        
                        logger.debug(f"Name result for {file_path}: {name_result.stdout}")
                        
                        if name_result.returncode == 0 and name_result.stdout:
                            app_name = name_result.stdout.strip().replace('Name=', '')
                            if app_name:
                                item_text = f"{app_name} ({file_path})"
                                logger.debug(f"Adding item: {item_text}")
                                self.app_listbox.addItem(item_text)
                                apps_found += 1
        
            if apps_found > 0:
                self.update_status(f"Found {apps_found} WSL application{'s' if apps_found != 1 else ''}")
            else:
                self.update_status("No WSL applications found. Try installing some GUI applications in WSL.", True)
                logger.warning("No applications found in WSL")
                
        except Exception as e:
            error_msg = f"Error loading applications: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.update_status(error_msg, True)

    def add_custom_application(self) -> None:
        """
        Open a dialog to add a custom WSL application.
        
        This method allows users to manually add applications that aren't
        automatically detected through .desktop files.
        """
        try:
            dialog = CustomAppDialog(self)
            if dialog.exec_():  # Dialog accepted if result is non-zero
                app_info: AppInfo = dialog.get_app_info()
                if not app_info:
                    self.update_status("No application information provided", True)
                    return
                
                name = app_info.get('name', '')
                command = app_info.get('command', '')
                icon = app_info.get('icon', None)
                
                if not name or not command:
                    self.update_status("Application name and command are required", True)
                    return
                    
                # Create item text with optional icon path
                item_text = f"{name} ({command})"
                if icon:
                    item_text += f"|{icon}"
                
                self.app_listbox.addItem(item_text)
                self.update_status(f"Custom application '{name}' added successfully")
                
                # Show success styling temporarily
                self.status_label.setStyleSheet("""
                    QLabel {
                        color: white;
                        background-color: """ + COLORS['success'] + """;
                        padding: 8px;
                        border-radius: 4px;
                        font-weight: bold;
                    }
                """)
                # Reset the style after 3 seconds
                QTimer.singleShot(3000, lambda: self.status_label.setStyleSheet(STYLES['status_label']))
                
        except Exception as e:
            error_msg = f"Error adding custom application: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.update_status(error_msg, True)

    def create_shortcut(self):
        """Create shortcuts for selected applications in the WSL default location"""
        selected_items = self.app_listbox.selectedItems()
        if not selected_items:
            self.status_label.setText("No application selected.")
            return
        
        if not self.distro_name:
            self.status_label.setText("No WSL distribution detected")
            return
        
        try:
            shortcut_dir = os.path.expandvars(f'%AppData%\\Microsoft\\Windows\\Start Menu\\Programs\\{self.distro_name}')
            if not os.path.exists(shortcut_dir):
                os.makedirs(shortcut_dir)
                
            for item in selected_items:
                app_info = item.text()
                parts = app_info.split('|')
                app_info = parts[0]
                icon_path = parts[1] if len(parts) > 1 else None
                
                app_name = app_info.split(' (')[0]
                app_path = app_info.split(' (')[1].rstrip(')')
                
                shortcut_path = os.path.join(shortcut_dir, f"{app_name}.lnk")
                
                # Check if this is a .desktop file or custom application
                is_desktop_file = app_path.endswith('.desktop')
                
                # Create the shortcut using the Windows Script Host with appropriate parameters
                with open('create_shortcut.vbs', 'w') as f:
                    if is_desktop_file:
                        # For .desktop files, use BAMF_DESKTOP_FILE_HINT
                        args = f'-d {self.distro_name} --cd ""~"" -- env BAMF_DESKTOP_FILE_HINT={app_path} {app_name.lower()}'
                    else:
                        # For custom applications, directly execute the command
                        args = f'-d {self.distro_name} --cd ""~"" -- {app_path}'
                    
                    icon_location = (
                        icon_path if icon_path 
                        else "C:\\Program Files\\WSL\\wslg.exe,0"
                    )
                    
                    f.write(f'''
                    Set WshShell = WScript.CreateObject("WScript.Shell")
                    Set shortcut = WshShell.CreateShortcut("{shortcut_path}")
                    shortcut.TargetPath = "C:\\Program Files\\WSL\\wslg.exe"
                    shortcut.Arguments = "{args}"
                    shortcut.WorkingDirectory = "%USERPROFILE%"
                    shortcut.WindowStyle = 1
                    shortcut.IconLocation = "{icon_location}"
                    shortcut.Description = "WSL GUI Application: {app_name}"
                    shortcut.Save
                    '''.strip())
                
                # Execute the VBS script
                subprocess.run(['cscript', '//Nologo', 'create_shortcut.vbs'], check=True)
                os.remove('create_shortcut.vbs')  # Clean up
                
            self.status_label.setText("Shortcut(s) created successfully.")
            
            # Refresh the shortcuts list
            self.shortcuts_listbox.clear()
            self.load_existing_shortcuts()
                
        except Exception as e:
            self.status_label.setText(f"Error creating shortcut: {str(e)}")

    def get_wsl_distro_info(self):
        """Get the default WSL distribution name and its Start Menu folder name"""
        try:
            # Get default distribution using different command format
            cmd = ['wsl.exe', '-l', '-v']
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-16le')
            print(f"WSL list output:\n{result.stdout}")  # Debug print
            
            # Parse the output line by line, handling UTF-16 encoding
            lines = [line for line in result.stdout.split('\n') if line.strip()]
            for line in lines[1:]:  # Skip header line
                if '*' in line:
                    # Split on multiple spaces and filter empty strings
                    parts = [part for part in line.split('  ') if part.strip()]
                    # The distribution name is the part after '*'
                    if len(parts) >= 1:
                        distro_name = parts[0].replace('*', '').strip()
                        print(f"Detected distribution: {distro_name}")  # Debug print
                        return distro_name, distro_name
            
            raise Exception("No default WSL distribution found")
        except Exception as e:
            error_msg = f"Error detecting WSL distribution: {str(e)}"
            print(error_msg)  # Debug print
            self.status_label.setText(error_msg)
            return None, None
        

    def _create_list_section(self, title: str, select_multiple: bool = False) -> Dict[str, Union[QVBoxLayout, QListWidget]]:
        """
        Create a section with a label and list widget.
        
        Args:
            title: The title for the section
            select_multiple: Whether to allow multiple selection in the list
            
        Returns:
            Dictionary containing the layout and list widget
        """
        layout = QVBoxLayout()
        
        # Create and style the label
        label = QLabel(title)
        label.setStyleSheet(STYLES['label'])
        layout.addWidget(label)
        
        # Create and style the list widget
        list_widget = QListWidget()
        list_widget.setStyleSheet(STYLES['list'])
        # Set selection mode using magic numbers (typing issues)
        mode = int(3) if select_multiple else int(1)  # ExtendedSelection=3, SingleSelection=1
        list_widget.setSelectionMode(mode)  # type: ignore
        layout.addWidget(list_widget)
        
        return {
            'layout': layout,
            'list': list_widget
        }