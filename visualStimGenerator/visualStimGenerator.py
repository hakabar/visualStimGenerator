
"""
Script to  generate visual stimuli on a screen/projector. It use the following
 - visualStimuliLib.py:    File containing all the classes of visual stimuli used.
 - expSettings.py:   File with the experiment settings (which type of visual stimulus plot and where) 
"""




import visualStimuliLib as generator
import expSettings as settings
import pygame as pg
import time
import yaml




def create_stimulus(stimToShow):
    #dict names
    typeStim=   settings.typeStim
    dispS=      settings.dispS
    dispP=      settings.dispP
    bckgndC=    settings.bckgndC
    color=      settings.color
    tSize=      settings.tSize
    matchTiles= settings.matchTiles
    horizonLvl= settings.horizonLvl
    rad=        settings.rad
    pos=        settings.pos
    rectW=      settings.rectW
    rectH=      settings.rectH


    #Draw the stimulus one
    if stimToShow[typeStim] == settings.typesOfShapes[0]:
        visualStim= generator.Checkerboard(stimToShow[dispS], stimToShow[dispP], stimToShow[bckgndC], stimToShow[color], stimToShow[tSize], stimToShow[matchTiles])
        print("match tiles to WA?  %s "%visualStim.get_matchTilesWA())
        visualStim.plot()
    elif stimToShow[typeStim] == settings.typesOfShapes[1]:
        visualStim= generator.Horizon(stimToShow[dispS], stimToShow[dispP], stimToShow[bckgndC], stimToShow[color], stimToShow[horizonLvl])
        visualStim.plot()
    elif stimToShow[typeStim] == settings.typesOfShapes[2]:
        visualStim= generator.Circle(stimToShow[dispS], stimToShow[dispP], stimToShow[bckgndC], stimToShow[color], stimToShow[pos], stimToShow[rad])
        visualStim.plot()
    elif stimToShow[typeStim] == settings.typesOfShapes[3]:
        visualStim= generator.Rectangle(stimToShow[dispS], stimToShow[dispP], stimToShow[bckgndC], stimToShow[color], stimToShow[pos], stimToShow[rectW], stimToShow[rectH])
        visualStim.plot()
    else:
        projection= generator.Stimulus()
        v1= generator.Rectangle()
        v2= generator.Circle()
    
        v1.plot(projection.get_surface())
        v2.plot(projection.get_surface())
    

    #Show the stimulus for a given time
    time.sleep(settings.displayDuration)
    #close Pygame window and exit
    pg.display.quit()
    pg.quit()



# ----- MAIN ----- 
for shape in settings.stimuli:
    create_stimulus(shape)