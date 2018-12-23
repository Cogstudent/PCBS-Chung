"""
An implementation of Povel and Essens: "Perception of Temporal Patterns" (1985). See README.pdf for further details.
The following code refers to an external .csv file in order to generate audio sequences and save them as independent audio files. The sequence is the following: (1) defining a specific sound signal; (2) reading the .csv file and converting the strins it contains into audio sequences of the tone; (4) saving the audio sequences as audio files.
"""


import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import write


def tone(freq, phase, duration, amplitude, SAMPLE_RATE):
    """The 'tone' function generates a sound wave according to specific values.

    Arguments
    ---------
    * freq: frequence of the wave in Hz - between 20Hz and 20,000Hz (float)
    * phase: position of the wave starting point in seconds (float)
    * duration: duration of the sound in seconds (float)
    * amplitude: amplitude of the wave (float)
    * SAMPLE_RATE: conversion rate in kHz - between 8kHz and 96kHz (float)

    Output
    ------
    * Sine wave (Numpy array)
    """
    t = np.linspace(0, duration, num = duration * SAMPLE_RATE)
    return amplitude * np.sin(2 * np.pi * freq * t - phase)


def csv_to_timings(filepath, interval):
    """The 'csv_to_timings' function opens a .csv file and converts each string of '0' and '1' it contains into a Numpy array of time values, where each value refers to the onset time of a tone.

    Argument
    --------
    * filepath: path to the .csv file that include a series of binary strings (string)
    * interval: length of the interval between two successive tones of the audio stimulus in seconds (float)

    Output
    ------
    * List of Numpy arrays, where each array refers to a series of time values defining a sound pattern (list)
    """
    file = open(filepath, 'r').read().split('\n')
    list_arrays = []
    for line in file:
        single_array = np.asarray([int(i) * interval for i, y in enumerate(line) if y == '1'])
        list_arrays.append(single_array)
    return list_arrays


def timings_to_audio(timings_array, tone):
    """The 'timings_to_audio' function computes an audio stimulus from a Numpy array and saves it into a dedicated folder as an audio file.

    Argument
    --------
    * array_timings: a series of time values defining a sound pattern (Numpy array)

    Output
    ------
    * Audio file of the stimulus named ‘audio*.wav’.
    """
    stimulus = np.zeros(round(NINTERVAL * INTERVAL_LENGTH * SAMPLE_RATE))
    for pos in timings_array:
        index = pos * SAMPLE_RATE
        stimulus[index:index+????????????????] = tone
    write('/stimuli/audio%d.wav' %(NPATTERN), SAMPLE_RATE, stimulus)

##########################

if __name__ == '__main__':
    SAMPLE_RATE = 22050 # in Hz
    INTERVAL_LENGTH = 0.07 # in seconds
    NINTERVAL = 16
    NPATTERN = 35

    clear_tone = tone(830, 0, 0.05, 0.5, SAMPLE_RATE)
    list_patterns = csv_to_timings('sound_patterns.csv', INTERVAL_LENGTH)
    for pattern in enumerate(list_patterns):
        timings_to_audio(pattern, clear_tone)
