"""This is the LinkedIn Level Up to schedule a function"""

#Three inputs: event time, function, any  number of arguments
# Requirements: sets alarm, plays sound file, and executes function
#schedule_function(time.time()+1, print, 'Howdy')
# pip install playsound

#from playsound import playsound
#from pydub import AudioSegment
#from pydub.playback import play

import datetime
import time
import sched


def schedule_function():

    #playing a sound
    #song = AudioSegment.from_wav("note.wav")
    #print('playing sound using pydub')
    #play(song)

 
    # using now() to get current time
    current_time = datetime.datetime.now()
    print("The current time on this computer is:", current_time)

    delay = input("Please the enter the time which you would like the function to run: ")
    
    s = sched.scheduler(time.localtime, time.sleep)
    s = (10000000, 3, print, "Howdy")
    print(s.scheduler.empty())


#webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Set up scheduler
#s = sched.scheduler(time.localtime, time.sleep)
# Schedule when you want the action to occur
#s.enterabs(time.strptime('Tue May 01 11:05:17 2018'), 0, action)
# Block until the action has been run
#s.run()

schedule_function()

