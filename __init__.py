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

from . import ui, ops

bl_info = {
    "name": "QT User Interface Demo",
    "author": "Nick Alberelli",
    "description": "Demo of a QT Interface inside of Blender",
    "blender": (4, 0, 0),
    "version": (0, 0, 1),
    "location": "3DView > Sidebar > QT UI Demo",
    "warning": "",
    "category": "Generic",
}


def register():
    ui.register()
    ops.register()


def unregister():
    ui.unregister()
    ops.unregister()
