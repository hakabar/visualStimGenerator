"""File containing the settings for each visual shape to be used as visual stimulus by the visualStimGenerator.py script.
    Developed by Diego Alonso San Alberto.
"""


#  ------ SHAPES AVAILABLE -----
typesOfShapes= ["checkerboard", "horizon", "circle", "rectangle"]

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

# ----- EXPERIMENT SETTINGS ----- 
# 0. Set the displayDuration values (in sec). Time the stimulus/stimuli will be plotted in the screen
# 1. Add as many dictionaties as shapes needed to be ploted
# 2. Add the name of the dictionaries to the stimuli list (at the end of the file)
# 3. Run python MainScript.py in the command line to plot the stimuli in defined in this file
displayDuration= 5   #number of seconds ploting each of the stimuli
    


shape1= {
    "type": typesOfShapes[0], 
    "tileSize": 20,
    "matchTilesWA": True, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }

shape2= {
    "type": typesOfShapes[1], 
    "horizonLvl": 3, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }

shape3= {
    "type": typesOfShapes[2], 
    "position": (100,100), 
    "radius": 30,
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }

shape4= {

    "type": typesOfShapes[3], 
    "position": (100,100), 
    "rectW": 60,
    "rectH": 90,
    "color": (120, 255,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }

h1= {
    "type": typesOfShapes[1], 
    "horizonLvl": 1, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }

h2= {
    "type": typesOfShapes[1], 
    "horizonLvl": 2, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }
h3= {
    "type": typesOfShapes[1], 
    "horizonLvl": 3, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }
h10= {
    "type": typesOfShapes[1], 
    "horizonLvl": 10, 
    "color": (120, 120,120), 
    "displaySurface": [600,400],
    "displayPosition": (150,50),
    "bckgndColor": (0,0,0)
    }
stimuli=[h1,h2,h3,h10]







