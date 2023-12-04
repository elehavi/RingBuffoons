# RingBuffoons
# Hello this is Wolfgang Hutton

##Functions we could add:
Overwriting: Each bin stores list of dictionaries. Each dictionary represents the spike count of each neuron after one loop thru the buffer/theta phase
 -- To do this, we need a helper function that creates a dict of neurons and theier spike counts at a given point.

 ##How to convey ring buffer quality..?

 ###Ring buffer
 - circle is oscillation.
 - 2 signals: spike and theta. one reads in one writes?
 - read and write intake measured data, put it into buffer, and the buffer loops and continually updates dictionary
 - bin ur in is reading. writing deposits spikes to be read out. 
 - at each loop: read takes in data. write sorts data into dictionary. 
 - getting data into buffer is write, read catches up and reads/sorts # of spikes
 -  