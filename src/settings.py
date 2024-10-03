import os
import wx

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TASKS_PATH = os.path.join(BASE_DIR, 'tasks', 'tasks.yaml')

ICON_PATH = os.path.join(BASE_DIR, 'assets', 'icons', 'adayacropped.ico')

IMAGES_PATH = os.path.join(BASE_DIR, 'assets', 'images')

DEFAULT_THEME = 0
