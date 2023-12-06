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
- Even if not entirely aligned in a way that would simulate the process by showing how the two components (theta and neuron) progress individually and simultaneously, still interesting that these two separate domains are conceptually relatable and that we can demonstrate the relationship through systems with properties that share a resemblence 




## Introduction 

This project began from interest spanning domains unfamiliar to each other, made enticing by what appeared to be beneath-surface-level counterparts between these previously separate domains. Namely, it appeared as if the computational ring buffer possessed qualities that aligned with those of the more neurobiological phase precession, as was seen in the papers and data from our assignments. These shared aspects seemed to include storage capacities, organization, and, most saliently, a relationship defined by an "offset" or delay.

In order to determine how we could implement phase precession within a ring buffer, we had to do further investigation on both ends and gain more details about the supposedly similar aspects

### Ring Buffers

A ring buffer is a data structure shaped like a circle with a predetermined number of slots. Ring buffers have a  Data streams, such as video streaming, use ring buffers beca

blah bla blah blah blah blah meow meow meow meow meow meow meow meow
### Phase Precession



### The Making of a Model

As we started to look at these similarities, we began to notice different properties, and thought about their purposes. 



From here on out, we began comparing the relationship between individual neurons and where in the theta phase, along with for how long, they fire. Based on what we could find in the literature, utilizing both text and figures and after much deliberation and changing of plans, we decided on intervals of pi/8. This would, in theory, allow us to somewhat capture the precise nature of the offsets while still being able to have more than one neuron and a subjectively reasonable amount of bins in our buffer. 


All that was left was to finalize what would be the read and what would be the write. 

### Hitting A Wall

This, though, is where we ran into what could be called the beginning of the end for our intertwining of these two domains. 

After all of our careful investigation, we determined that the similarities are just that-- similarities. In reality, one is a cause, and one is an effect. 

The ring buffer's offset is a specific mechanic that serves a purpose-- a means to the end that is INSERT PURPOSE HERE. Meanwhile, the offset between the neuron and theta rhythm is an end due to the previously discussed biological means.

While the offset relationship between the neuron and theta cycle could be expressed by using the theta phase for bins, or by using position bins coupled with respective read and writes for both the neuron and theta cycle, that merely takes advantage of the ring buffer's components as tools to paint a picture, not to simulate a process that aligns with those components' properties. There is no choice we could find that would reconcile matching the neuron and cycle to either the read or write while still preserving the properties of each system. It also would not be accurate to even say that the neurobiological components and the ring buffer components serve different purposes, as the neurobiological components-- given our current knowledge-- are better described as phenomena than tools. Additionally, the neuroscience components and their relationship make up (for the sake of interpretation) one simultaneous process in which we are observing two things occur at the same time and noticing the offset between them. Meanwhile, the read and write perform two different processes. Their offset enables them to accomplish a single overarching goal of data SOMETHING LIKE TRANSFER AND ORGANIZATION but they operate separately, reemphasizing how this offset is a tool, while the other is a consequence. 

We really hated to leave it on this note, wanting so desperately to find a solution that would allow this connection to be made. Alas, it seemed that trying to force a connection was tenuous at best. That doesn't mean we can't appreciate the similarities and connections we *did* find, though. We started off this journey, for lack of a better term, being genuinely excited about combining our experience with our respective fields and mixing together elements that seemed remarkably similar given the differences in their contexts. (This "remarkability", of course, was because it was too good to be true). If it did work, it would have been a fascinating connection to make, but arguably, ending on this note requires us to have gone through far more critical thinking, deliberation, and exploration in this unique topic that we wouldn't have otherwise. Our means led us to a different end than we originally expected, and while frustrating and unfamiliar and truly a battle between determination and humility, it was a valuable experience. Now knowing that this connection may not be fulfilled in the way we anticipated, we can appreciate how these domains (which were even more separate than we originally realized) resemble each other. I mean, there are penguins in completely different parts of the world in different temperatures, and they're both cool? I know that metaphor is about as tenuous as our original model proposal, but you get the point. Our defeat, I suppose, does not defeat how interesting the similarities are, even if this is where they end. 

