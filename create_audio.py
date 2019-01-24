"""
An implementation of Povel and Essens: "Perception of Temporal Patterns" (1985). See README.pdf for further details.
The following code refers to an external .csv file in order to generate audio sequences and save them as independent audio files. The sequence is the following: (1) defining a specific sound signal; (2) reading the .csv file and converting the strings it contains into audio sequences; (3) saving the audio sequences as audio files.
"""


import numpy as np
from scipy.io.wavfile import write
import os

SAMPLE_RATE = 22050 # in Hz - between 8kHz and 96kHz 
INTERVAL_LENGTH = 0.3 # in seconds - length of each time-onset in a pattern
NINTERVAL = 16 # number of time-onsets in a pattern
NPATTERN = 35 # number of temporal patterns


def tone(freq, phase, duration, amplitude, sample_rate):
    """The 'tone' function generates a sound wave according to specific values.

    Arguments
    ---------
    * freq: frequence of the wave in Hz - between 20Hz and 20,000Hz (float)
    * phase: position of the wave starting point in seconds (float)
    * duration: duration of the sound in seconds (float)
    * amplitude: amplitude of the wave (float)
    * sample_rate: conversion rate in kHz - between 8kHz and 96kHz (float)

    Output
    ------
    * Sine wave (Numpy array)
    """
    t = np.linspace(0, duration, num = duration * SAMPLE_RATE)
    return amplitude * np.sin(2 * np.pi * freq * t - phase)


def csv_to_timings(filepath, interval):
    """The 'csv_to_timings' function opens a .csv file and converts each string of '0' and '1' it contains into a Numpy array of time values, where each value refers to the emission of a tone (a beat).

    Argument
    --------
    * filepath: path to the .csv file that includes a series of temporal patterns encoded in "0" and "1" (string)
    * interval: length of each time-onset in a temporal pattern (float)

    Output
    ------
    * List of Numpy arrays, where each array refers to a series of time values defining a temporal pattern (list)
    """
    file = open(filepath, 'r').read().split('\n')
    list_arrays = []
    for line in file:
        single_array = np.asarray([int(i) * interval for i, y in enumerate(line) if y == '1'])
        list_arrays.append(single_array)
    return list_arrays


def timings_to_audio(timing_arrays, interval, len_array, tone, sample_rate):
    """The 'timings_to_audio' function computes an audio stimulus from a Numpy array and saves it as an audio file.

    Argument
    --------
    * timings_arrays: a series of arrays (Numpy array)
    * narray: number of arrays, each defining a temporal pattern (int)
    * interval: length of each time-onset in a temporal pattern(float)
    * len_array: number of time values in a series (int)
    * tone: sound to associate with each time value of the series (Numpy array)
    * sample_rate: conversion rate in kHz (float)

    Output
    ------
    * Audio file of the stimulus named ‘audio*.wav’.
    """
    file_number = 0
    for array in timing_arrays:
        file_number += 1
        stimulus = np.zeros(int(interval * len_array * sample_rate))
        for pos in array:
            index = int(pos * sample_rate)
            stimulus[index : (index + len(tone))] = tone
        while os.path.isfile('audio%d.wav' %(file_number)):
            file_number += 1 # to avoid erasing existing stimuli files
        write('audio%d.wav' %(file_number), sample_rate, stimulus)

##########################

if __name__ == '__main__':
    clear_tone = tone(830, 0, 0.05, 0.5, SAMPLE_RATE)
    list_patterns = csv_to_timings('sound_patterns.csv', INTERVAL_LENGTH)
    timings_to_audio(list_patterns, INTERVAL_LENGTH, NINTERVAL, clear_tone, SAMPLE_RATE)
