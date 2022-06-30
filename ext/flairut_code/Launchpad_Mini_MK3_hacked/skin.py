# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: c:\Jenkins\live\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Mini_MK3\skin.py
# Compiled at: 2020-10-03 01:14:59
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import merge_skins, Skin
from ableton.v2.control_surface.elements import Color
from novation.colors import Rgb
from novation.skin import skin as base_skin

class Colors:
    
    # For the select track hack
    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.WHITE_HALF
    
    # For the arm track hack
    class Mixer:
        ArmOn = Rgb.PURPLE
        ArmOff = Rgb.PURPLE_HALF
    
    class Mode:

        class Session:
            Launch = Color((Rgb.PALE_GREEN_HALF.midi_value, Rgb.WHITE_HALF.midi_value))
            Overview = Color((Rgb.BLUE.midi_value, Rgb.WHITE_HALF.midi_value))
    
            


skin = merge_skins(*(base_skin, Skin(Colors)))