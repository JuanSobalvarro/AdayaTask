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


def resource_path(relative_path):
    """ Get the absolute path to the resource in the app directory. """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller extraction folder
        base_path = sys._MEIPASS
    else:
        # Base directory when running from source
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)

def get_tasks_path():
    """ Returns the absolute path to the tasks.yaml file. """
    return resource_path(os.path.join('tasks', 'tasks.yaml'))

def get_icon_path():
    """ Returns the absolute path to the application icon file. """
    return resource_path(os.path.join('assets', 'icons', 'adayacropped.ico'))

def get_images_path():
    """ Returns the absolute path to the images directory. """
    return resource_path(os.path.join('assets', 'images'))
