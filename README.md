# <u>**Programing for Cognitive and Brain Science**
## Final project - Victor Chung

> *Please note that my project is a work in progress as I am still facing several issues. Since we have last discussed in class, I have been able to fix the first part of my code (generating audio stimuli) but I am still facing some problems in the second part of my code (displaying stimuli and recording subject's performance). For details of the problems to fix, see section IV.*


### Introduction
This project aims to replicate the first experiment introduced in "Perception of Temporal Patterns" ([Povel & Essens, 1985](http://mp.ucpress.edu/content/2/4/411)). This seminal paper has provided with new insights on music perception for Povel and Essens have hypothesized that humans generate an internal clock while listening to a temporal pattern. To test this hypothesis, they offer to measure the ability to perceive and reproduce tone sequences that differ with respect to their tone-onset intervals (or rhythm). The authors' hypothesis suggests a correlation between the subject's performance and the category the temporal pattern belongs to: the more different from the subject's internal clock the pattern is, the more difficult the task is and the poorer the subject's performance.

The experiment consists in generating 7 categories of 5 temporal patterns each, before presenting those audio stimuli to a subject. The subject is able to listen to the temporal pattern with no limit of time. Once the subject feels ready, one is asked to reproduce the temporal pattern 4 times in a row with the computer keyboard. Simultaneously, the program records the subject's preparation time (while listening to the temporal pattern) and the subject's performance (while reproducing the temporal pattern). Then the subject shall move to the next pattern. The complete experiment (35 stimuli) is estimated to last about 50 minutes.
<br>

### I. Algorithm
The implementation of this experiment relies on two main steps: (1) generating audio stimuli and (2) displaying those stimuli to a subject, whose task consists in reproducing that stimuli. For ease and accuracy of the replication, I will input Povel and Essens' original patterns in a .csv files instead of generating new temporal patterns randomly. As a result, one can distinguish between several steps:

**(1a)** creating a tone that will serve as a basic component for the audio stimuli.
**(1b)** reading a .csv file that contains several strings of "0" and "1" and converting each string into a pattern of rhythm, that is: a series of timings that refer to the beats.
**(1c)** applying the tone to each beat of those series of timings and saving those sound sequences into .wav files.
**(2a)** displaying randomly each audio stimulus to the subject.
**(2b)** asking the subject to reproduce the audio stimulus.
<br>

### II. Description of the program
The two steps described above are associated with two distinct files.

#### (1) create_audio.py
ipso

#### (2) pulsation.py
ipso
<br>

### III. Instructions for use
1. Make sure the folder contains the file `sounds_patterns.csv`. The same folder should also include the two python files that are mentioned below.

2. Call `create_audio.py` to generate the 35 audio files that corresponds to the stimuli. The audio files will be saved in the same folder.

3. Call `pulsation.py` to launch the Expyriment's interface and start the experiment.
<br>

### IV. To do

**Main problem**
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

I am still trying to make sense of this error message but the numerous related threads I have found online suggests issues that are related to the configuration of Pygame (such as faulty installation) rather than an error in the program.

**Improvements**
* Audio files are correctly read by audio players such as iTunes but fail to be correctly read by other players such as VLC.
* Ideally, the functions I define in `create_audio.py` should be called as modules in `pulsation.py` to streamline the process.
* `pulsation.py` should also provide with basic analysis of the preparation time and the subject's performance thanks via Numpy and Matplotlib.

<br>

### Ending notes
* **Level in programming before the class:** I had no previous knowledge of programming whatsoever but the basics learned during class last september.
* **Skills learned during the class:**
* **Suggestions:**
