# visualStimGenerator
Python script to create and plot different visual stimulus shapes with PyGame
It use the following files:
 - visualStimLib.py:    File containing all the classes of visual stimuli used.
 - expSettings.py:   File with the experiment settings (which type of visual stimulus plot and where) 
 - visualStimGenerator.py: Main code to read the settings of the experiment defined in expSettings.py and create the requested visual stimulus/stimuli from the stimuli classes defined in visualStimGenerator.py
 
 The current types of cisual stimuli that can create this software are:
 """Checkerborad
    - tileSize:         Size of the checkerboard tiles (in pixels)
    - matchTilesWA:     If True the drawing surface expand to be filled by full tiles. If False the end of the drawing surface can be filled with partial tiles
    - color:            Color assigned to the visual stimulus
    - displaySurface:   [width, height] of the PyGame window (where the stimulus will be drawed)
    - displayPosition:  Postion in the screen/projection of the PyGame window
    - bckgndColor:      Color to fill the PyGame windows as background    
"""
""" Horizon
    - horizonLvl:       Level of the horizon in the PyGame window. It will cover 1/horizonLvl of the PyGame window
    - color:            Color assigned to the visual stimulus
    - displaySurface:   [width, height] of the PyGame window (where the stimulus will be drawed)
    - displayPosition:  Postion in the screen/projection of the PyGame window
    - bckgndColor:      Color to fill the PyGame windows as background  

"""
""" Circle
    - position:         Position of the center of the circle in the PyGame window
    - radius:           Radius of the circle
    - color:            Color assigned to the visual stimulus
    - displaySurface:   [width, height] of the PyGame window (where the stimulus will be drawed)
    - displayPosition:  Postion in the screen/projection of the PyGame window
    - bckgndColor:      Color to fill the PyGame windows as background  

"""
""" Rectangle
    - position:         Position of the corner top left of the rectangle in the PyGame window
    - rectW:            Width of the rectangle
    - rectH:            Height of the rectangle
    - color:            Color assigned to the visual stimulus
    - displaySurface:   [width, height] of the PyGame window (where the stimulus will be drawed)
    - displayPosition:  Postion in the screen/projection of the PyGame window
    - bckgndColor:      Color to fill the PyGame windows as background  

"""
