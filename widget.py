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
    QPushButton,
    QDialog,
)


class Ui_ShowGroupWidget(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.setupUi()
        self.roiGroups = {}
        # self.data = data
        self.submit_fn = callback
        self.Submit.clicked.connect(self.submitclose)

    def setupUi(self):
        # sets up Submit button
        self.Submit = QPushButton("Submit", self)

    def submitclose(self):
        # do whatever you need with self.roiGroups
        try:
            data = {"keys": "values"}
            self.submit_fn(data)
        except:
            raise
        self.accept()
