"""Constants and styles for the UI components."""

from typing import Dict

# Define color scheme
COLORS: Dict[str, str] = {
    "primary": "#2196F3",  # Material Blue
    "secondary": "#FFC107",  # Material Amber
    "success": "#4CAF50",  # Material Green
    "danger": "#F44336",  # Material Red
    "background": "#FFFFFF",  # White
    "text": "#212121",  # Dark Grey
    "disabled": "#9E9E9E",  # Grey
}

# Define selection modes
SELECTION_MODE: Dict[str, int] = {
    "no_selection": 0,
    "single": 1,
    "multi": 2,
    "extended": 3,
    "contiguous": 4,
}

# Define styles
STYLES: Dict[str, str] = {
    "button": f"""
        QPushButton {{
            background-color: {COLORS['primary']};
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: #1976D2;
        }}
        QPushButton:pressed {{
            background-color: #0D47A1;
        }}
        QPushButton:disabled {{
            background-color: {COLORS['disabled']};
        }}
    """,
    "danger_button": f"""
        QPushButton {{
            background-color: {COLORS['danger']};
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: #D32F2F;
        }}
        QPushButton:pressed {{
            background-color: #B71C1C;
        }}
    """,
    "list": f"""
        QListWidget {{
            background-color: white;
            border: 1px solid #BDBDBD;
            border-radius: 4px;
            padding: 4px;
        }}
        QListWidget::item {{
            padding: 8px;
            margin: 2px 0;
        }}
        QListWidget::item:selected {{
            background-color: {COLORS['primary']};
            color: white;
            border-radius: 2px;
        }}
        QListWidget::item:hover:!selected {{
            background-color: #E3F2FD;
            border-radius: 2px;
        }}
    """,
    "label": f"""
        QLabel {{
            color: {COLORS['text']};
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 8px;
        }}
    """,
    "status_label": f"""
        QLabel {{
            color: {COLORS['text']};
            font-size: 12px;
            padding: 8px;
            background-color: #F5F5F5;
            border-radius: 4px;
        }}
    """,
}
