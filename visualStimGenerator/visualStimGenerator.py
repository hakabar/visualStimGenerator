
"""
Script to  generate visual stimuli on a screen/projector. It use the following
 - visualStimuli.py:    File containing all the classes of visual stimuli used.
 - confExperiment.py:   File with the experiment settings (which type of visual stimulus plot and where) 
"""




import visualStimLib as generator
import confExperiment as settings
import pygame as pg
import time
import yaml






def test_classes(index, stimuli):
    stimToShow=stimuli[index]
    displayDuration= 5   #number of seconds ploting the stimulus

    #Draw the stimulus one
    if stimToShow == stimuli[0]:
        visualStim= generator.Checkerboard()
        print("match tiles to WA?  %s "%visualStim.get_matchTilesWA())
        visualStim.plot()
    elif stimToShow == stimuli[1]:
        visualStim= generator.Horizon()
        visualStim.plot()
    elif stimToShow == stimuli[2]:
        visualStim= generator.Circle()
        visualStim.plot()
    elif stimToShow == stimuli[3]:
        visualStim= generator.Rectangle()
        visualStim.plot()
    else:
        projection= generator.Stimulus()
        v1= generator.Rectangle()
        v2= generator.Circle()
    
        v1.plot(projection.get_surface())
        v2.plot(projection.get_surface())
    

    #Show the stimulus for a given time
    time.sleep(displayDuration)
    #close Pygame window and exit
    pg.display.quit()
    pg.quit()



def test_from_dict(stimToShow):
    #dict names
    typeStim= 'type'
    dispS= 'displaySurface'
    dispP= 'displayPosition'
    bckgndC= 'bckgndColor'
    color= 'color'
    tSize= 'tileSize'
    matchTiles= 'matchTilesWA'
    horizonLvl= 'horizonLvl'
    rad= 'radius'
    pos= 'position'
    rectW= 'rectW'
    rectH= 'rectH'


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

#data={}

# Read YAML file
#with open("test.yaml", 'r') as stream:
#    data_loaded = yaml.load(stream)
#    prettyprint(data_loaded)


#stimuli= ['checkerboard', 'horizon', 'circle', 'rectangle', 'circle_and_rectangle']
for shape in settings.stimuli:
    test_from_dict(shape)