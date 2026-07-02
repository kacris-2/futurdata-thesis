"""
Unit tests for AddColorDialog.

Run from the project root (futurdata-thesis/):
    python -m unittest src.tests.test_add_color_dialog -v
"""

import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from main.views.add_color_dialog import AddColorDialog

class TestAddColorDialog(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.controller = MagicMock()

    def tearDown(self):
        self.root.destroy()

    @patch('main.views.add_color_dialog.AddColorDialog.wait_window')
    @patch('main.views.add_color_dialog.AddColorDialog.grab_set')
    def test_init(self, mock_grab, mock_wait):
        dialog = AddColorDialog(self.root, self.controller)
        self.assertIsInstance(dialog.name_var, tk.StringVar)
        self.assertIsInstance(dialog.hex_var, tk.StringVar)
        self.assertEqual(dialog.title(), "Add New Color")
        mock_grab.assert_called_once()
        mock_wait.assert_called_once_with(dialog)

    @patch('main.views.add_color_dialog.AddColorDialog.wait_window')
    @patch('main.views.add_color_dialog.AddColorDialog.grab_set')
    @patch('main.views.add_color_dialog.colorchooser.askcolor')
    def test_choose_color(self, mock_askcolor, mock_grab, mock_wait):
        dialog = AddColorDialog(self.root, self.controller)
        mock_askcolor.return_value = ((255.0, 128.0, 0.0), '#ff8000')
        dialog.choose_color()
        self.assertEqual(dialog.hex_var.get(), '#ff8000')
        self.assertEqual(dialog.rgb_r_var.get(), '255')
        self.assertEqual(dialog.rgb_g_var.get(), '128')
        self.assertEqual(dialog.rgb_b_var.get(), '0')

    @patch('main.views.add_color_dialog.AddColorDialog.wait_window')
    @patch('main.views.add_color_dialog.AddColorDialog.grab_set')
    def test_on_save_success(self, mock_grab, mock_wait):
        dialog = AddColorDialog(self.root, self.controller)
        dialog.destroy = MagicMock()
        
        dialog.name_var.set("Orange")
        dialog.hex_var.set("#ff8000")
        dialog.rgb_r_var.set("255")
        dialog.rgb_g_var.set("128")
        dialog.rgb_b_var.set("0")
        
        dialog.on_save()
        self.controller.add_new_color.assert_called_once_with("Orange", "#ff8000", 255, 128, 0)
        dialog.destroy.assert_called_once()

    @patch('main.views.add_color_dialog.AddColorDialog.wait_window')
    @patch('main.views.add_color_dialog.AddColorDialog.grab_set')
    def test_on_save_missing_fields(self, mock_grab, mock_wait):
        dialog = AddColorDialog(self.root, self.controller)
        dialog.name_var.set("")
        dialog.on_save()
        self.controller.add_new_color.assert_not_called()

if __name__ == '__main__':
    unittest.main()
