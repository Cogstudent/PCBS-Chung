"""
An implementation of Povel and Essens: "Perception of Temporal Patterns" (1985). See README.pdf for further details.
This program present a series of audio stimuli to the suject, who has to reproduce the rythm of the audio sequence after each stimulus. The program records the performances of the subject.
"""

import glob
import expyriment as xpy
from expyriment.stimuli import Audio, BlankScreen
expyriment.control.defaults.audiosystem_sample_rate = 22050 # to avoid any mismatch with the sample rate of the audio files

from expyriment import control # test
control.set_develop_mode(True) # test

##########################

INSTRUCTIONS1 = """You will take part in a simple experiment about the sense of rythm, which involves listening to a series of rythmic patterns and reproducing them with the computer keyboard.The chronological sequence will be the following:
1. The computer plays a rythmic pattern on a loop. Feel free to tap on the table with your finger while you memorize the pattern.
2. When you feel you have listened to the rythmic pattern long enough to reproduce it, press the any button on the keyboard to stop the sound.
3. The computer asks you to reproduce the rythmic pattern by pressing the ay keyboard buttton in rythm. Please keep reproducing the pattern until the computer says it is over.
4. Press any button on the keyboard to move on to the next rythmic pattern.
Note: you can leave at any time by pressing the ESC button."""
INSTRUCTIONS2 = "Please listen to the rythmic pattern and try to memorize it. When you feel ready, press any button on the keyboard."
INSTRUCTIONS3 = "Whenever you are ready, try to reproduce the rythmic pattern you have just heard by pressing any button on the keyboard in rythm. Please keep reproducing the rythmic pattern until the computer says it is over."
INSTRUCTIONS4 = "Please press any button on the keyboard to start."
INSTRUCTIONS5 = "Please press any button on the keyboard to move on to the next pattern."
BACKGROUND2 = "(Playing sound...)"
BACKGROUND1 = "(Recording...)"

##########################

### INITIALIZE THE EXPERIMENT
exp = xpy.design.Experiment(name = "Pulsation")
xpy.control.initialize(exp)
exp.add_data_variable_names = ["category", "button", "prep_time"]

kb = xpy.io.Keyboard()
bs = xpy.stimuli.BlankScreen(colour = (0, 0, 0))


### DESIGN THE EXPERIMENT
block = xpy.design.Block()
for audiofile in glob.glob('audio*.wav'):
    trial = xpy.design.Trial()
    trial.add_stimulus(xpy.stimuli.Audio(audiofile))
    if audiofile == 'audio[1-5]':
        trial.set_factor('category', '1')
    elif audiofile == 'audio[6-10]':
        trial.set_factor('category', '2')
    elif audiofile == 'audio[11-15]':
        trial.set_factor('category', '3')
    elif audiofile == 'audio[16-20]':
        trial.set_factor('category', '4')
    elif audiofile == 'audio[21-25]':
        trial.set_factor('category', '5')
    elif audiofile == 'audio[26-30]':
        trial.set_factor('category', '6')
    elif audiofile == 'audio[31-35]':
        trial.set_factor('category', '7')
    block.add_trial(trial)
block.shuffle_trials()

### DEFINE INSTRUCTIONS
instructions1 = xpy.stimuli.TextScreen("Welcome!", text = INSTRUCTIONS1)
instructions2 = xpy.stimuli.TextScreen("Instructions", text = INSTRUCTIONS2)
instructions3 = xpy.stimuli.TextScreen("Instructions", text = INSTRUCTIONS3)
instructions4 = xpy.stimuli.TextScreen("Instructions", text = INSTRUCTIONS4)
instructions5 = xpy.stimuli.TextScreen("Instructions", text = INSTRUCTIONS5)
background_sound = xpy.stimuli.TextScreen("---", text = BACKGROUND1)
background_answer = xpy.stimuli.TextScreen("---", text = BACKGROUND2)

### PRESENT INSTRUCTIONS
instructions1.preload()
instructions1.present()
instructions4.preload()
kb.wait()
instructions4.present()
kb.wait()

### START THE EXPERIMENT
xpy.control.start()
for trial in block.trials:

    # PART 1 - Playing the audio stimulus
    instructions2.present()
    background_sound.preload()
    exp.clock.wait(1000 - trial.stimuli[0].preload())
    kb.wait()
    background_sound.present()
    key, rt = kb.wait(callback_function = trial.stimuli[0].play()) # play the audio stimuli as long as the subject hasn't pressed any button
    xpy.control.wait_end_audiosystem()
    exp.data.add([trial.get_factor('category'), key, rt])
    bs.present()

    # PART 2 - Recording the subject's performance (/!\ NOT IMPLEMENTED YET)
    #instructions3.present()
    #background_answer.preload()
    #exp.clock.reset_stopwatch()
    #kb.wait()
    #background_answer.present()
    #instructions5.present()
    #kb.wait()


### END THE EXPERIMENT
xpy.control.end(goodbye_text = "Thank you very much for participating in our experiment.", goodbye_delay = 5000)
