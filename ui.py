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
from bpy.types import Panel
from .ops import QTDEMO_OT_show_ui


class QTDEMO_PT_ui(Panel):
    """Basic UI in Blender that contains the Operator to Launch QT Interface."""

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QT UI Demo'
    bl_label = "QT UI Demo"

    def draw(self, context):
        self.layout.operator(QTDEMO_OT_show_ui.bl_idname)


def register():
    bpy.utils.register_class(QTDEMO_PT_ui)


def unregister():
    bpy.utils.unregister_class(QTDEMO_PT_ui)
