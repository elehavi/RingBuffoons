# RingBuffoons

## Functions we could add:
Overwriting: Each bin stores list of dictionaries. Each dictionary represents the spike count of each neuron after one loop thru the buffer/theta phase
 -- To do this, we need a helper function that creates a dict of neurons and theier spike counts at a given point.

 ## How to convey ring buffer quality..?

 ### Ring buffer
 - circle is oscillation.
 - 2 signals: spike and theta. one reads in one writes?
 - read and write intake measured data, put it into buffer, and the buffer loops and continually updates dictionary
 - bin ur in is reading. writing deposits spikes to be read out. 
 - at each loop: read takes in data. write sorts data into dictionary. 
 - getting data into buffer is write, read catches up and reads/sorts # of spikes


 - biggest similarity: if u represent this way, the point where it starts a new loop is where spiking occurs at same point in theta rhythm
 -- lagging... then next time it fires = when it "overwrites"


 - writing can b faster than read
 -- imagine 1 buffer per neuron. it becomes overwritten when it stops being part of the scene.
 -- start at 1 extreme, go to other extreme, then be done.
 -- write is less than 1 cycle ahead of the read. when write is more than 1 cycle ahead of read, then that neuron is no longer functioning/silent
 -- then what are bins? theta vs spike count

 - Mar's levels -- what level vs how level vs computation aspect/why
 - ring buffer contexts. memory access
 - here is our mapping of variables.

FINAL WRITE UP BELOW

# Ring Buffer Explanation
Ella

# Phase Precession Components 

# What initially seems connected 

# Possible way of implementing phase precession in ring buffer

# What this implementation do?
- Marr's Levels - what has been typically looked at, how does this mapping combine various fields

# Not entirely concrete, since there are aspects of each that don't necessarily allow for a direct modeling of the process, but there are interesting similarities between the two realms to be interesting from a conceptual standpoint. The two have not been mixed in the past, may be helpful in conceptualization, interesting connections from somewhat separate domains


