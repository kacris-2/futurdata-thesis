"""
Unit tests for AddToolDialog.

Run from the project root (futurdata-thesis/):
    python -m unittest src.tests.test_add_Tool_dialog -v
"""

import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from main.views.add_tool_dialog import AddToolDialog

class TestAddToolDialog(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.controller = MagicMock()

    def tearDown(self):
        self.root.destroy()

    @patch('main.views.add_tool_dialog.AddToolDialog.wait_window')
    @patch('main.views.add_tool_dialog.AddToolDialog.grab_set')
    def test_init(self, mock_grab, mock_wait):
        dialog = AddToolDialog(self.root, self.controller)
        self.assertEqual(dialog.title(), "Add New Tool")
        mock_grab.assert_called_once()
        mock_wait.assert_called_once_with(dialog)

    @patch('main.views.add_tool_dialog.AddToolDialog.wait_window')
    @patch('main.views.add_tool_dialog.AddToolDialog.grab_set')
    def test_on_save_success(self, mock_grab, mock_wait):
        dialog = AddToolDialog(self.root, self.controller)
        dialog.destroy = MagicMock()
        
        dialog.name_var.set("Power Drill")
        dialog.category_var.set("Power Tools")
        
        dialog.on_save()
        self.controller.add_new_tool.assert_called_once_with("Power Drill", "Power Tools")
        dialog.destroy.assert_called_once()

    @patch('main.views.add_tool_dialog.AddToolDialog.wait_window')
    @patch('main.views.add_tool_dialog.AddToolDialog.grab_set')
    def test_on_save_missing_name(self, mock_grab, mock_wait):
        dialog = AddToolDialog(self.root, self.controller)
        dialog.name_var.set("")
        dialog.category_var.set("Hand Tools")
        
        dialog.on_save()
        self.controller.add_new_tool.assert_not_called()

if __name__ == '__main__':
    unittest.main()
