"""
Package containing different classes to be used as visual stimuli with PyGame
  - Stimulus:       Main class. It contains all the information regarding the PyGame windows and drawing surface
  - Checkerboard:   Subclass. It creates a checkerboard pattern in the surface provided by Stimulus. 
                    The checkerboard can fit the surface (the surface will increase it size to match) or not (must be specified in the settings) 
  - horizon:        Subclass. It creates a horizon pattern in the surface provided by Stimulus
  - Circle:         Subclass. It creates a circle pattern in the surface provided by stimulus
  - Rectangle:      Subclass. It creates a rectangle pattern in the surface provided by Stimulus
The clasess Circle and Rectangle can plot several of them together (regardless their classes) in the same surface provided by Stimulus
"""

import pygame as pg
import os, math
import time



class Stimulus(object):

    def __init__(self, dispS, dispP, bckgndC):        
        self.displaySurface=dispS
        self.displayPosition=dispP
        self.bckgndColor= bckgndC    #(0,0,0)== BLack -- (255,255,255)== WHITE
        self.surface= pg.Surface((self.displaySurface[0],self.displaySurface[1]))
        self.workingArea= self.initialize_WA()

    #Initialize working area (PyGame window)
    def initialize_WA(self):
        pg.init()
        #Define where to create the pygame working window/area (by using SDL environment variables)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.displayPosition[0], self.displayPosition[1])
        return pg.display.set_mode((self.displaySurface[0], self.displaySurface[1]), pg.NOFRAME)

    def get_width(self):
        return self.displaySurface[0]
    def get_height(self):
        return self.displaySurface[1]
    def get_bckgndColor(self):
        return self.bckgndColor
    def get_surface(self):
        return self.surface
    def get_workingArea(self):
        return self.workingArea

    def set_width(self, w):
        self.width=w
    def set_height(self, h):
        self.height=h
    def set_bckgndColor(self, c):
        self.bckgndColor= c
        #self.surface.fill(self.bckgndColor)


    def fill_bckgndColor(self):
        self.surface.fill(self.bckgndColor)

    #Change the width and height of a given surface. This is quicker if you want to repeatedly scale something.
    def modify_surface(self, w, h):
        self.surface= None
        self.width=w
        self.height=h
        self.surface= pg.Surface((w,h))        

    #Function to update the PyGame window (working area)
    def update_wa(self, update):
        self.workingArea.blit(update, (0,0))
        pg.display.update()



class Checkerboard(Stimulus):

    def __init__(self,  dispS, dispP, bckgndC, color, tileS, match):
            super(Checkerboard, self).__init__(dispS, dispP, bckgndC)
            self.tileSize= tileS
            self.matchTilesWA= match
            self.visualColor= color
    
    def get_tileSize(self):
        return self.tileSize
    def get_matchTilesWA(self):
        return self.matchTilesWA
    def get_color(self):
        return self.visualColor

    def set_tileSize(self, sz):
        self.tileSize= sz   
    def set_matchTilesWA(self, m):
        #matchTilesWA can be only True or False
        self.matchTilesWA= m
    def set_color(self, c):
        self.visualColor= c


    # Draw a checkerboard in the defined working area
    def plot(self, srfc=None):
        #if division is not exact, we need to round to next higher integer
        self.totalCellsW= int(math.ceil(float(super(Checkerboard, self).get_width())/self.tileSize))
        self.totalCellsH= int(math.ceil(float(super(Checkerboard, self).get_height())/self.tileSize))
        #Create the sheckerboard surface
        if self.matchTilesWA == True:
            self.matchTilesWA='kkdvak'
            #the display Surface will be able to draw all the squares completely
            super(Checkerboard, self).modify_surface(self.tileSize*self.totalCellsW, self.tileSize*self.totalCellsH)
        #Fill the surface with background color
        super(Checkerboard, self).fill_bckgndColor()   
        #Fill with visualColor the corresponding tiles
        for x in range(0, self.totalCellsW):
            for y in range(0, self.totalCellsH, 2):
                #to display the white squares correctly in the odds rows
                if x%2 != 0:
                    y+=1
                self.stimulus= pg.draw.rect(self.surface, self.visualColor, (x*self.tileSize, y*self.tileSize, self.tileSize, self.tileSize))
        #Update the working area (PyGame window)
        super(Checkerboard,self).update_wa(self.surface)




class Horizon(Stimulus):
    def __init__(self,dispS, dispP, bckgndC, color,lvl):
        super(Horizon, self).__init__(dispS, dispP, bckgndC)
        self.horizonLvl= lvl   #Level of the horizon bigger value, smaller horizon
        self.visualColor= color

    def get_color(self):
        return self.visualColor
    def get_horizonLvl(self):
        return self.horizonLvl

    def set_color(self, c):
        self.visualColor= c
    def set_horizonLvl(self, h):
        self.horizonLvl= horizonLvl
    
    # Draw a checkerboard in the defined working area
    def plot(self):
        #Starting px vale for the horizon height
        self.horizonLine= super(Horizon, self).get_height()/self.horizonLvl
        #Fill it with background color
        super(Horizon, self).fill_bckgndColor()    
        #Draw the type of visual stimulus in the given position
        pg.draw.rect(self.surface, self.visualColor, (0, super(Horizon, self).get_height()-self.horizonLine, super(Horizon, self).get_width(), self.horizonLine))
        #Update the working area (PyGame window)
        super(Horizon,self).update_wa(self.surface)




class Circle(Stimulus):

    def __init__(self, dispS, dispP, bckgndC, color, pos, rad):
        super(Circle, self).__init__(dispS, dispP, bckgndC)
        self.radius= rad
        self.position= pos
        self.visualColor= color

    def get_radius(self):
        return self.radius
    def get_position(self):
        return self.position
    def get_color(self):
        return self.visualColor
    
    def set_radius(self, r):
        self.radius= r
    def set_position(self, p):
        #position must be a TUPLE as (x,y)
        self.position= p
    def set_color(self):
        self.visualColor= c

    def plot(self, srfc=None):
        #Fill it with background color
        super(Circle, self).fill_bckgndColor()
        if srfc== None:
            surfaceUsed= super(Circle, self).get_surface()
        else:
            surfaceUsed= srfc
        #Draw the type of visual stimulus in the given position
        pg.draw.circle(surfaceUsed, self.visualColor, self.position, self.radius)
        #Update the working area (PyGame window)
        super(Circle, self).update_wa(surfaceUsed)



class Rectangle(Stimulus):

    def __init__(self, dispS, dispP, bckgndC, color, pos, w, h):
        super(Rectangle, self).__init__(dispS, dispP, bckgndC)
        self.rectW= w
        self.rectH= h
        self.position=pos
        self.visualColor= color

    def get_rectW(self):
        return self.rectW
    def get_rectH(self):
        return self.rectH
    def get_position(self):
        return self.position
    def get_color(self):
        return self.visualColor
    
    def set_rectW(self, w):
        self.rectW= w
    def set_rectH(self, h):
        self.rectH= h
    def set_position(self, p):
        #position must be a TUPLE as (x,y)
        self.position= p
    def set_color(self, c):
        self.visualColor= c

    def plot(self, srfc= None):
        #Fill it with background color
        super(Rectangle, self).fill_bckgndColor()
        if srfc== None:
            surfaceUsed= super(Rectangle, self).get_surface()
        else:
            surfaceUsed= srfc
        #Create the figure used as visual stimulus
        pg.draw.rect(surfaceUsed, self.visualColor, (self.position, (self.rectW, self.rectH)))
        #Update the working area (PyGame window)
        super(Rectangle, self).update_wa(surfaceUsed)