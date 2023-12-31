## Ring Buffoons

This file serves as a blanket overview of various aspects of our process, and is in line with our presentation. (https://docs.google.com/presentation/d/1cBr9ZH9MvSdAnh0Ur0QkBS4tPLOSGWuVXpVqagUUfrw/edit?usp=sharing) 
As most of our project can be conveyed through our actual presentation, this exists more as a supplementary refresher/summary. 

### Introduction 

This project began from interest spanning domains unfamiliar to each other, made enticing by what appeared to be beneath-surface-level counterparts between these previously separate domains. Namely, it appeared as if the computational ring buffer possessed qualities that aligned with those of the more neurobiological phase precession, as was seen in the papers and data from our assignments. These shared aspects seemed to include storage capacities, organization, and, most saliently, a relationship defined by an "offset" or delay.

To determine how we could implement phase precession within a ring buffer, we had to do further investigation on both ends and gain more details about the supposedly similar aspects:

### Ring Buffers

A ring buffer is a data structure shaped (conceptually) like a circle with a predetermined number of slots. Ring buffers usually have two pointers: a write pointer and a read pointer. The write pointer takes data and write it into slots of the buffer, while the read pointer looks at data in the buffer and write it out to another destination. To ensure that no data is overwritten before it is read, the write pointer must not lap the read buffer and must be less than the sum of the read pointer's location and size of the buffer. Alternatively, to ensure that no data is reread, the read buffer must always be less than the write buffer.

Data streams, such as video streaming, use ring buffers because of its first in, first out properties and maximum size. In the example of video streaming, the write pointer would take clips of a video and store them in slots in the ring buffer, and the read pointer would read those clips onto a user's computer. This way, the video streaming service does not need to send the whole video at once, which would take more time than sending it in pieces using a buffer. 

Our original goal entailed using a dictionary in each bin involving the neuron spike count (and which neurons the spikes belong to), as aligned with periods of the theta cycle. 

Note: Phase precession is detailed in the slides, but we felt it might be appropriate to describe ring buffers here.

### The Making of a Model

As we started to look at these similarities, we began to notice different properties of the two systems and thought about their purposes. 

From here on out, we compared the relationship between individual neurons and where in the theta phase, along with for how long, they fire. Based on what we could find in the literature, utilizing both text and figures and after much deliberation and changing of plans, we decided on intervals of pi/8 (later changed to pi/4 for practicality). This would, in theory, allow us to somewhat capture the precise nature of the offsets while still being able to have more than one neuron and a subjectively reasonable amount of bins in our buffer. After formulating a plan to generate spikes in a Gaussian distribution for each neuron, we wanted to reevaluate the soundness of our "model" and finalize the components. All that was left was to settle upon what would be the read and what would be the write. 

### Hitting A Wall

This, though, is where we ran into what could be called the beginning of the end for our intertwining of these two domains. After all of our careful investigation, we determined that the similarities are just that-- similarities. In reality, one is a cause, and one is an effect. The ring buffer's offset is a specific mechanic that serves a purpose-- a means to the end. Meanwhile, the offset between the neuron and theta rhythm is an end due to the previously discussed (in slides) biological means.

While the offset relationship between the neuron and theta cycle could be expressed by using the theta phase for bins, or by using position bins coupled with respective read and writes for both the neuron and theta cycle, that merely takes advantage of the ring buffer's components as tools to paint a picture, not to simulate a process that aligns with those components' properties. There is no choice we could find that would reconcile matching the neuron and cycle to either the read or write while still preserving the properties of each system. It also would not be accurate to even say that the neurobiological components and the ring buffer components serve different purposes, as the neurobiological components-- given our current knowledge-- are better described as phenomena than tools. Additionally, the neuroscience components and their relationship make up (for the sake of interpretation) one simultaneous process in which we are observing two things occur at the same time and noticing the offset relationship between them. Even though the offset may serve a purpose for temporal and spatial memory consolidation, it does not appear to exist specifically for that reason. Meanwhile, the read and write perform two different processes. Their offset enables them to accomplish a single overarching goal, but they operate separately on *one set/stream of data*, reemphasizing how *this* offset is a tool, while the other is a consequence. 


We really hated to leave it on this note, wanting so desperately to find a solution that would allow this connection to be made. Alas, it seemed that trying to force a connection was tenuous at best. That doesn't mean we can't appreciate the similarities and connections we *did* find, though. We started off this journey, for lack of a better term, being genuinely excited about combining our experience with our respective fields and mixing elements together that seemed remarkably similar given the differences in their contexts. (This "remarkability", of course, was because it was too good to be true after investigation). If it did work, it would have been a fascinating connection to make, but arguably, ending on this note requires us to have gone through far more critical thinking, deliberation, and exploration in this unique topic that we wouldn't have otherwise looked into to this degree. Our means led us to a different end than we originally expected, and while frustrating and unfamiliar and truly a battle between determination and humility, it was a valuable experience. Now knowing that this connection may not be fulfilled in the way we anticipated, we can appreciate how these domains (which were even more separate than we originally realized) resemble each other. Our defeat, we suppose, does not invalidate how interesting the similarities are, even if this is where they end. In the end, being *confident* about why we were wrong became our goal, and it was incredibly rewarding to be able to articulate this lack of a relationship convincingly. 

---

## Code Documentation

This section outlines the code in the Python files included in this repository.

### ringbuffer.py

This file lays out the definition for a ring buffer class in Python, where each slot represents a certain interval and contains the firing rate of certain neurons in said interval. Users can construct a ring buffer by passing the number of neurons and the size of the interval. Here are the member variables of the class:

* __binSize__ : This variable is passed into the constructor and determines the size of each bin.
* __numNeurons__ : Similarly, this variable is passed to the constructor and lays out the number of neurons.
* __numBins__ : This variable represents the number of bins. To calculate this variable, we use 6π for the first neuron, and add an additional 2π for the rest of the neurons. Then, we divide that sum by the size of each bin to find the number of bins we are creating.
* __data__ : This variable contains a python array representing the slots in our buffer. Each 'slot' has a dictionary, where the keys represent the neurons and the value of each neuron is its spike count in the current bin.
* __oldest__ and __curpos__ : These two pointers represent the oldest untouched bin, and the current bin that we are updating. These two pieces of ring buffer functionality are less applicable to our neuroscience context.

Additionally, we have an "add" function that takes in an ordered list of integers, representing the spike count of each neuron, and translates that into the spike count of the neurons in the bin indexed by curpos.

### gptbuffer.py

This file is the result of passing our code into chatGPT and asking it to generate spikes from a gaussian. In addition to the aforementioned functionality, this file includes the function "gaussian_spike_count," which takes in a phase and generates a number of spikes.
