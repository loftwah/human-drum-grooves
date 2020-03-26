#!/usr/bin/python
# Uses python3


import sys

import os
import time

import magenta.music as mm
from visual_midi import Plotter


def generate_plot_from_midi(sequence, file_name, file_id):
    # Writes the resulting plot file to the output directory
    date_and_time = time.strftime('%Y-%m-%d_%H%M%S')
    plot_filename = "%s_%s_%s.html" % (file_name, file_id,
                                       date_and_time)
    plot_path = os.path.join("/Users/reiners/Dropbox/projects/human-drum-grooves/output", plot_filename)
    pretty_midi = mm.midi_io.note_sequence_to_pretty_midi(sequence)
    plotter = Plotter()
    plotter.save(pretty_midi, plot_path)
    print(f"Generated plot file: {os.path.abspath(plot_path)}")


def load_sequence_from_midi(midi_file_name):
    note_sequence = mm.midi_io.midi_file_to_note_sequence(midi_file_name)

    return note_sequence


def main(midi_file_name, plot_name, plot_id):
    sequence = load_sequence_from_midi(midi_file_name)
    generate_plot_from_midi(sequence, plot_name, plot_id)


if __name__ == "__main__":
    args = sys.argv[1:]
    input_midi_file_name = args[0]
    output_file_name = args[1]
    output_file_id = args[2]
    main(input_midi_file_name, output_file_name, output_file_id)
