# <u>Programing for Cognitive and Brain Science
## Final project - Victor Chung

> *Please note that my project is a work in progress as I am still facing several issues. Since we have last discussed in class, I have been able to fix the first part of my code (generating audio stimuli) but I am still facing some problems in the second part of my code (displaying stimuli and recording subject's performance). For details of the problems to fix, see section IV.*

***
### Introduction
This project aims to replicate the first experiment introduced in "Perception of Temporal Patterns" ([Povel & Essens, 1985](http://mp.ucpress.edu/content/2/4/411)). This seminal paper has provided with new insights on music perception for Povel and Essens have hypothesized that humans generate an internal clock while listening to a temporal pattern. To test this hypothesis, they offer to measure the ability to perceive and reproduce tone sequences that differ with respect to their tone-onset intervals (or rhythm). The authors' hypothesis suggests a correlation between the subject's performance and the category the temporal pattern belongs to: the more different from the subject's internal clock the pattern is, the more difficult the task is and the poorer the subject's performance.

The experiment consists in generating 7 categories of 5 temporal patterns each, before presenting those audio stimuli to a subject. The subject is able to listen to the temporal pattern with no limit of time. Once the subject feels ready, one is asked to reproduce the temporal pattern 4 times in a row with the computer keyboard. Simultaneously, the program records the subject's preparation time (while listening to the temporal pattern) and the subject's performance (while reproducing the temporal pattern). Then the subject shall move to the next pattern. The complete experiment (35 stimuli) is estimated to last about 50 minutes.

***
### I. Algorithm
The implementation of this experiment relies on two main steps: (1) generating audio stimuli and (2) displaying those stimuli to a subject, whose task consists in reproducing that stimuli. For ease and accuracy of the replication, I will input Povel and Essens' original patterns in a .csv files instead of generating new temporal patterns randomly. As a result, one can distinguish between several steps:

**(1a)** creating a tone that will serve as a basic component for the audio stimuli.

**(1b)** reading a .csv file that contains several strings of "0" and "1" and converting each string into a pattern of rhythm, that is: a series of timings that refer to the beats.

**(1c)** applying the tone to each beat of those series of timings and saving those sound sequences into .wav files.

**(2a)** displaying randomly each audio stimulus to the subject.

**(2b)** asking the subject to reproduce the audio stimulus.

***
### II. Instructions for use
1. Make sure the folder contains the file `sounds_patterns.csv`. The same folder should also include the two python files that are mentioned below.

2. Call `create_audio.py` to generate the 35 audio files that correspond to the stimuli. The audio files will be saved in the same folder.

3. Call `pulsation.py` to launch the Expyriment's interface and start the experiment.

***
### III. Description of the program
The two steps described above are associated with two distinct files.

#### (1) create_audio.py
`tone` function defines a Numpy array that corresponds to a sound wave. The different parameters (frequence, phase, amplitude, duration) are set to match the original experiment, which relies on a A-tone.

`csv_to_timings`refers to a pre-existing .csv file, which contains strings of "0" and "1", where each "0" stands for a silence and each "1" for the emission of a tone (a beat). The first step consists in opening the .csv file and splitting its content into multiple strings. The second step converts each string into an integer and multiply this integer by the length of an interval for each beat. The outputs are single arrays that are progressively added to an empty list.

`timings_to_audio` associates the A-tone to every beat of each single array. For each single array of timing values, the program creates an empty Numpy array whose size is converted into an integer to avoid any error message. Then the program fills this empty Numpy array with the A-tone according to the timing of the beats. The output is a stimulus that is saved as an audio file.


#### (2) pulsation.py
Each audio stimuli is associated with a category: since they have been generated according to the order of the .csv file, they are orderly grouped in 7 groups of 5 stimuli. The category is an important factor since it determines the level of difficulty to reproduce the temporal patterns. However, the stimuli will be presented in a random order so that the impact of the difficulty on the performance is distinguishable from the impact of habituation or attention weakening.

The experiment starts with main instructions before moving on to the random presentation of the audio stimuli. For each stimulus, the subject goes through two parts: first, listening to the stimulus and then, reproducing the stimulus.
**[First part]** Once the subject is ready, the program plays the audio stimulus in loop as long as the subject doesn't press a button on the computer keyboard. During this first part, the program starts collecting basic data: the button pressed by the subject and the total time the subject has spent listening to the stimulus. One hypothesizes that the latter (preparation time of the subject) will positively correlate with the level of difficulty (category of the stimulus).
**[Second part]** As an introduction to the second part, the program reminds the instructions that ask the subject to reproduce the rhythmic stimulus with the computer keyboard. Here, the program waits for the subject to reproduce the stimuli 4 times, that is: the computer waits for a single button to be pressed approximately 40 times in a row. During this second part, the program will start a clock and records each time the subject press a button. These time values append an empty list that represents the subject's reproduction of the stimulus. As upcoming update, the program should be able to assess the difference between each time value of a series of 4 and then it should compare this difference with the difference between each beat of the original stimulus. One hypothesizes that the average difference for each subject's performance will increase with the number of the category.

***
### IV. To do

#### (1) Main problem
The main issue I am facing is an error in the execution of `pulsation.py`: the experiment goes as expected until the program has to load or play the audio stimuli. The error message is the following:

```
WARNING:  140: This application, or a library it uses, is using the deprecated  Carbon Component Manager for hosting Audio Units. Support for this will be removed in a future release. Also, this makes the host incompatible with version 3 audio units. Please transition to the API's in AudioComponent.h.
Fatal Python error: (pygame parachute) Segmentation Fault
Current thread 0x00007fff7b807000 (most recent call first):
File "/anaconda3/lib/python3.6/site-packages/expyriment/stimuli/_audio.py", line 109 in preload
File "pulsation.py", line 85 in <module>
Abort trap: 6
```

Although I am not really worried about the "Warning", I have tried to address the "Segmentation fault" with the following modifications:
1. I have tried to preload the audio stimuli with `xpy.stimuli.Audio(audiofile).preload` earlier in the program (in the design body before starting the experiment), assuming that the program had not enough time to preload the audio files. Result: same error message.
2. I have updated Pygame from 10.0.1 to 19.0.1 with `pip install --upgrade pip`. Result: same error message.

I am still trying to make sense of this error message but the numerous related threads I have found online are suggesting issues that are related to the configuration of Pygame (such as a faulty installation) rather than an error in the program.

#### (2) Improvements
* Audio files are correctly read by audio players such as iTunes but fail to be correctly read by other players such as VLC.
* Ideally, the functions I define in `create_audio.py` should be called as modules in `pulsation.py` to streamline the process.
* The second part of the experiment in `pulsation.py` is to be completed so that the program waits for a button to be pressed about 40 times (4 repetitions of a temporal pattern) while the program records the exact time clock of each button pressure and append a list that will consists in the timing values of the subject's performance.
* `pulsation.py` should also provide with basic analysis of the preparation time and the subject's performance thanks via Numpy and Matplotlib.

***
### Ending notes
* **Level in programming before the class:**
I had no previous knowledge of programming whatsoever but the basics learned during class last September.


* **Skills learned during the class:**
    1. I hope I have learned to write code properly, that is: finding a balance between informing about one's code and achieving accuracy and conciseness in doing so. I am also starting to grasp what "pythonesque" means although I feel there is a lot of room for improvement. I also think I could do better in calling functions as modules in other programs.
    3. I have also learned, among other things:
        * to use the shell
        * to use ipython
        * to use Github
        * to open and save files in a Python program
        * to use pandas, glob, Numpy, Expyriment, Pygame
        * to create audio and visual stimuli and to display them via Pygame or Expyriment
        * to gather data, compute basic statistics from a Numpy array and display the results with Matplotlib.


* **Suggestions:**  
    1. Perhaps it would have been easier to start the final project a bit earlier (session 0 to create a Github repository and commit to a project on mid-November) so that one would have had more time to meet other people and help each other out. Although I have been posting some messages on Slack, I have met some of my colleagues in person and this seems easier and more efficient than copying-pasting chunks of code on Slack.
    2. I have been confused more than once by the alternation between Schoology and Slack as official communication channels: I would rather focus on one platform without any preference regarding the above mentioned ones.
    3. Regarding the exercises, I like the distinction between core exercises and optional ones. During class, one could focus on only one major exercise/program that subsumes all the major difficulties and tricks for each chapter (e.g. visual stimuli, audio, data analysis, experiments), leaving the correction of small exercises to indivdual time.
