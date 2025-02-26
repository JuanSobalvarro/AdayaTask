# src/helpers/paths.py

import logging
import sys
import os


def exception(path):
    """Handle exceptions related to file paths."""
    try:
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError(f"Path not found: {path}")
    except Exception as e:
        logging.error(f"Error accessing path: {path}. Exception: {e}")
        return None

class Paths:
    @staticmethod
    def resource_path(relative_path):
        """ Get the absolute path to the resource in the app directory. """
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller extraction folder
            base_path = sys._MEIPASS
        else:
            # Base directory when running from source
            base_path = os.path.abspath('.')

        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_tasks_path():
        """ Returns the absolute path to the tasks.yaml file. """
        return Paths.resource_path(os.path.join('tasks', 'tasks.yaml'))

    @staticmethod
    def get_icon_path():
        """ Returns the absolute path to the application icon file. """
        return Paths.resource_path(os.path.join('assets', 'icons', 'adayacropped.ico'))

    @staticmethod
    def get_images_path():
        """ Returns the absolute path to the images' directory. """
        return Paths.resource_path(os.path.join('assets', 'images'))

    @staticmethod
    def get_settings_path():
        return Paths.resource_path(os.path.join('config', 'settings.yaml'))