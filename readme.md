# Average Photo Booth
A Raspberry Pi photobooth which averages the user's portrait with all other participants.

## Technologies
* A Python script using guizero provides the user interface. 
* the gphoto2 software package provides out of the box control over a connected DSLR camera.
* imagemagick is used to resize incoming files to a more managable size, so they don't take too long to average
* (Facetool.py)[https://github.com/hay/facetool] provides a convenient wrapper for OpenCV, Tensorflow, dlib, and other complex libraries used to do the face averaging operation. Although installing the dependencies for Facetool was complicated (dependency hell) it was much simpler to get up and running than using straight OpenCV.
