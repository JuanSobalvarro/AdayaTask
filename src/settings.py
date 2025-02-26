# settings.py

from .helpers.paths import Paths
import yaml

# Default settings
DEFAULT_SETTINGS = {
    'theme': 0,  # 0 = Light, 1 = Dark
    'tasks_path': Paths.get_tasks_path(),
    'icon_path': Paths.get_icon_path(),
    'images_path': Paths.get_images_path(),
    'settings_path': Paths.get_settings_path(),
}

# Load settings from a YAML file
def load_settings():
    try:
        with open(Paths.get_settings_path(), 'r') as file:
            settings = yaml.safe_load(file)
            return settings
    except FileNotFoundError:
        return DEFAULT_SETTINGS  # Return defaults if no settings file is found

# Save settings to a YAML file
def save_settings(settings):
    with open(Paths.get_settings_path(), 'w') as file:
        yaml.safe_dump(settings, file)
