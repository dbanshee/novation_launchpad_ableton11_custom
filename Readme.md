# Novation Launchpad Mini MK3 - Ableton11 Custom MIDI Remote Script to Arm an Select Tracks

This project adapts the original **Reddit/Flairuts** Custom MIDI Remote Script  for **Novation Launchpad Mini MK3** to **Ableton11**.

It hacks the Ableton default Script adding features from *Launchpad X*. Now Session View adds **Arm** and **Select** Tracks options.

<div style="text-align:center"><img src=./images/novation_launchpad_mini_mk3.jpeg /></div>


## Original Resource
- Flairuts Hack
https://www.reddit.com/r/ableton/comments/ly1xfk/novation_launchpad_mini_mk3_flariuts_arm_and/



## Installation
1. Copy the folder `src/Launchpad_Mini_MK3_Custom` to the User Library Remote scripts folder of your local Ableton installation.
On windows Tipically

```
C:\Users\...\Documents\Ableton\User Library\Remote Scripts\
```

2. On Ableton Preferences select `Launchpad_Mini_MK3_Custom` as your surface control.

3. Now on the Session View, the cyclical mode Button `Stop/Solo/Mute` has 2 new options: `Stop/Solo/Mute/Arm/Select`

## Issues on Development

Possibly a decompilation issue from python bytecode are detailed here:

https://github.com/gluon/AbletonLive11_MIDIRemoteScripts/issues/4


## Additional Resources

- https://structure-void.com/ableton-live-midi-remote-scripts/
- https://github.com/laidlaw42/ableton-live-midi-remote-scripts
- http://remotescripts.blogspot.com/
- https://medium.com/@ibekso/ableton-scripts-34d615c37aa2
- https://medium.com/@ibekso/ableton-user-remote-scripts-75cc413c21b8
- https://github.com/gluon/AbletonLive11_MIDIRemoteScripts


## Extra Information
### Ableton Config

```
C:\Users\...\AppData\Roaming\Ableton\Live 11.0\Preferences\Options.txt
--------------------------------------------------------------------------
-EnableArmOnSelection
```
    
### Ableton Develop

Ableton User Remote Scripts
```
C:\Users\..\AppData\Roaming\Ableton\Live 11.0\Preferences\User Remote Scripts
```

Ableton Log
```
less /cygdrive/c/Users/.../AppData/Roaming/Ableton/Live\ 11.0/Preferences/Log.txt
```

Ableton Remote Scripts Folder
```
C:\Users\...\Documents\Ableton\User Library\Remote Scripts\
```
