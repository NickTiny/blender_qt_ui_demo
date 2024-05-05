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

import bpy
from bpy.types import Operator, Timer
from PySide6.QtWidgets import QApplication
from .widget import Widget


class QTDEMO_OT_show_ui(Operator):
    """
    Blender Operator to that will invoke QT interface. This a 'Modal'
    operator which means it allows the user to continue to interact with
    Blender while the operator and QT Interface are running.

    """

    bl_idname = "qtdemo.show_ui"
    bl_label = "Show QT UI"
    bl_description = """Show custom QT UI"""

    _app: QApplication = None
    _widget: Widget = None
    _timer: Timer = None

    def modal(self, context, event):
        # Finish running operator if window is closed
        if not self._widget.isVisible():
            context.window_manager.event_timer_remove(self._timer)
            return {'FINISHED'}
        else:
            # Procecess any events
            self._app.processEvents()
        return {'PASS_THROUGH'}

    def execute(self, context):
        # Create instance of app if it exists (allows for multiple windows)
        self._app = QApplication.instance()
        if not self._app:
            self._app = QApplication()

        # Show QT Widget
        self._widget = Widget()
        self._widget.show()

        # Timer controls when modal() function is called
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.05, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}


def register():
    bpy.utils.register_class(QTDEMO_OT_show_ui)


def unregister():
    bpy.utils.unregister_class(QTDEMO_OT_show_ui)
