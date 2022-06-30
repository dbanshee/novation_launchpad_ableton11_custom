# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 18 2021, 16:00:48) 
# [GCC 10.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Mini_MK3\__init__.py
# Compiled at: 2020-01-30 13:18:25
# Size of source mod 2**32: 894 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .launchpad_mini_mk3 import Launchpad_Mini_MK3
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661,
                          product_ids=[275],
                          model_name=['Launchpad Mini MK3']), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[NOTES_CC, REMOTE]),
                 outport(props=[NOTES_CC, SYNC, SCRIPT]),
                 outport(props=[REMOTE])]}


def create_instance(c_instance):
    return Launchpad_Mini_MK3(c_instance=c_instance)
# okay decompiling __init__.pyc
