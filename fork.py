"""
demo.py - demonstration program for freq2note.py
by William H. Grover | wgrover@engr.ucr.edu | http://groverlab.org
"""

import freq2note as f2n

freqs = [67.877,]
notes = ""

for f in freqs:
    notes = notes + f2n.lilypond(f2n.find_closest_note(f))

f2n.write(notes)
