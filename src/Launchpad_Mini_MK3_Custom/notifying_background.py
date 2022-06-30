# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 18 2021, 16:00:48) 
# [GCC 10.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Mini_MK3\notifying_background.py
# Compiled at: 2020-04-28 23:37:54
# Size of source mod 2**32: 618 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v2.control_surface.components import BackgroundComponent

class NotifyingBackgroundComponent(BackgroundComponent):
    __events__ = ('value', )

    def register_slot(self, control, *a):
        super(BackgroundComponent, self).register_slot(control, partial(self._NotifyingBackgroundComponent__on_control_value, control), 'value')

    def __on_control_value(self, control, value):
        self.notify_value(control, value)
# okay decompiling notifying_background.pyc
