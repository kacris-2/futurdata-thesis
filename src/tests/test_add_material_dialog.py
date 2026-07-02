"""
Unit tests for AddMaterialDialog.

Run from the project root (futurdata-thesis/):
    python -m unittest src.tests.test_add_material_dialog -v
"""

import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from main.views.add_material_dialog import AddMaterialDialog

class TestAddMaterialDialog(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.controller = MagicMock()
        self.controller.db.get_all_colors.return_value = [
            {'id': 1, 'name': 'Red'},
            {'id': 2, 'name': 'Blue'}
        ]

    def tearDown(self):
        self.root.destroy()

    @patch('main.views.add_material_dialog.AddMaterialDialog.wait_window')
    @patch('main.views.add_material_dialog.AddMaterialDialog.grab_set')
    def test_init(self, mock_grab, mock_wait):
        dialog = AddMaterialDialog(self.root, self.controller)
        self.assertEqual(dialog.title(), "Add New Material")
        self.assertDictEqual(dialog.color_map, {'Red': 1, 'Blue': 2})
        mock_grab.assert_called_once()
        mock_wait.assert_called_once_with(dialog)

    @patch('main.views.add_material_dialog.AddMaterialDialog.wait_window')
    @patch('main.views.add_material_dialog.AddMaterialDialog.grab_set')
    def test_on_save_success(self, mock_grab, mock_wait):
        dialog = AddMaterialDialog(self.root, self.controller)
        dialog.destroy = MagicMock()
        
        dialog.name_var.set("Oak Wood")
        dialog.sci_name_var.set("Quercus")
        dialog.color_var.set("Blue")
        
        dialog.on_save()
        self.controller.add_new_material.assert_called_once_with("Oak Wood", "Quercus", 2)
        dialog.destroy.assert_called_once()

    @patch('main.views.add_material_dialog.AddMaterialDialog.wait_window')
    @patch('main.views.add_material_dialog.AddMaterialDialog.grab_set')
    def test_on_save_missing_name(self, mock_grab, mock_wait):
        dialog = AddMaterialDialog(self.root, self.controller)
        dialog.name_var.set("")
        dialog.color_var.set("Red")
        
        dialog.on_save()
        self.controller.add_new_material.assert_not_called()

if __name__ == '__main__':
    unittest.main()
