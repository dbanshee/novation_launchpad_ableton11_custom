# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 18 2021, 16:00:48) 
# [GCC 10.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Mini_MK3\skin.py
# Compiled at: 2021-02-15 23:01:01
# Size of source mod 2**32: 666 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import merge_skins, Skin
from ableton.v2.control_surface.elements import Color
from novation.colors import Rgb
import novation.skin as base_skin

class Colors(object):

    class Mode(object):

        class Session(object):
            Launch = Color((Rgb.PALE_GREEN_HALF.midi_value, Rgb.WHITE_HALF.midi_value))
            Overview = Color((Rgb.BLUE.midi_value, Rgb.WHITE_HALF.midi_value))


skin = merge_skins(base_skin, Skin(Colors)*())
# okay decompiling skin.pyc
