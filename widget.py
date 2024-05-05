# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
from PySide6.QtGui import QIcon


class Widget(QWidget):
    """A custom QT main window using PySide6 shows an example of a user interface."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Main Window")
        self.setWindowIcon(QIcon.fromTheme("applications-development"))

        label = QLabel("Text: ")
        self.line_edit = QLineEdit()

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        button = QPushButton("Print to Console")
        button.clicked.connect(self.button_clicked)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)

        self.setLayout(v_layout)


def button_clicked(self):
    """Prints the text entered in the line edit widget to the console."""
    print(self.line_edit.text())
