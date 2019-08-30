
"""
Script to  generate visual stimuli on a screen/projector. It use the following
 - visualStimuliLib.py:    File containing all the classes of visual stimuli used.
 - expSettings.py:   File with the experiment settings (which type of visual stimulus plot and where) 
"""

import visualStimuliLib as generator
import expSettings as settings
import pygame as pg
import time

import multiprocessing as mp




def create_stimulus(stimToShow):
    try: 
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

        #Show the stimulus for a given time
        time.sleep(settings.displayDuration)
        #close Pygame window and exit
        pg.display.quit()
        pg.quit()

    except Exception as e:
        print(" * ERROR! \n")
        print('   %s'%e)



# ----- MAIN ----- 
if __name__== '__main__':
    totalStim= len(settings.stimuli)
    print(' * Creating %s visual stimuli'%(totalStim))
    
    #Create a pool of processes and assign a process for each visual stimulus
    proc= mp.Pool(totalStim)
    proc.map(create_stimulus,[settings.stimuli[i] for i in range(totalStim)])

#  ----- END -----


