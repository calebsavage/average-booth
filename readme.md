# Average Photo Booth
A Raspberry Pi photobooth which averages the user's portrait with all other participants.

## About
This is a project created for **Making Media Making Devices**, a 1-credit weekend course at (NYU ITP)[https://itp.nyu.edu] taught by Matt Richardson. 

## Why?
I'm a photo person and have always found photobooths fascinating. The old-school chemical variety are my favorites-- the mechanism is incredibly cool. But I'm also fascinated by what the booth itself sees (I've always had a tendancy to anthropomorphize machines) and what each customer leaves behind. 

This project examines privacy in public spaces and the afterlife of images (and imagemaking). It may or may not function as a metaphor for human relationships. 

Instead of delivering a self-portrait on a blank slate, the program delivers the user's face blended with all the faces before theirs. As more people use the photobooth, each person's likeness impacts the average slightly less than the person before them.

It forces a confrontation with the unseen forces of the past which shape our future through an endless series of small coincidences. 

## Process

I began by setting up a rudimentary photobooth app during the in-class exercises. I was excited by the format, and decided I wanted to create a strange version of the familiar device. I expiremented with the OpenCV library, which was exciting but rather complicated to dive into. I found the Facetool utility online, which provided a very convenient interface for some more complex computer vision functionality.
 I didn't have a Pi camera of my own and didn't want to purchase one when I have an old-but-functional DSLR sitting on the shelf, so I looked into Gphoto2 to control a DSLR from the Pi and found it easier than expected. 

## Technologies
* A Python script using guizero provides the user interface. 
* the gphoto2 software package provides out of the box control over a connected DSLR camera.
* imagemagick is used to resize incoming files to a more managable size, so they don't take too long to average
* (Facetool.py)[https://github.com/hay/facetool] provides a convenient wrapper for OpenCV, Tensorflow, dlib, and other complex libraries used to do the face averaging operation. Although installing the dependencies for Facetool was complicated (dependency hell) it was much simpler to get up and running than using straight OpenCV.

## Challenges
* Installing the dependencies for Facetool took hours. I struggled for a long time with wrangling Python versions in order to install the Poetry dependency manager packaged with it, and eventually gave up entirely and loaded all the required modules with Pip.
* When getting ready to make a video documentation, I fried my SD card by unplugging the Pi while it was being written to. I was able to recover my data, but need to reinstall the OS and that's how the dog ate my homework this week. I hope this written documentation will suffice.

## Next Steps
I was surprised how well this idea came together and I have vague plans to develop it into a more polished project. It would work best contained in some sort of box or cabinet which is somewhat portable, and incorporates the screen, camera, and control device (touchscreen or buttons). 

Visually, I'd like to expirment with ways of showing how the average face has changed over time and create a more polished GUI.
