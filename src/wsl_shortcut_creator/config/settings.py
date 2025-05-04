"""Configuration management for WSL Shortcut Creator."""
import os
from typing import Dict, Any

class Settings:
    """Application settings manager."""
    
    def __init__(self):
        self._config: Dict[str, Any] = {
            'app_name': 'WSL Shortcut Creator',
            'shortcuts_dir': os.path.expandvars('%AppData%\\Microsoft\\Windows\\Start Menu\\Programs'),
            'resources_dir': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
        }
    
    def get(self, key: str) -> Any:
        """Get a configuration value."""
        return self._config.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self._config[key] = value

# Global settings instance
settings = Settings()
