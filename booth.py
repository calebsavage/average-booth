from guizero import App, Picture, PushButton, Window
import os
import time

def recompute_avg():
    print("deleting old avg.jpg")
    cmd1 = "rm avg.jpg"
    os.system(cmd1)
    print("averaging")
    cmd = "./facetool/facetool.py average -i ./facetool/input -o avg.jpg"
    
    os.system(cmd)
    
    pic.value="avg.jpg"
    return True


def capture_image():

    filename = 'facetool/input/'+str(time.time()).replace('.','')+'.jpg'
    print("taking pic filename: "+filename)
    cmd = 'gphoto2 --filename "'+filename+'" --capture-image-and-download'
    os.system(cmd)
    print("resizing")
    cmd2 = "convert -resize 20% "+filename+" "+filename
    os.system(cmd2)
    
    
    
    print("displaying pic "+filename)
    pic.value = filename
    
    
    return True
def both():
    capture_image()
    recompute_avg()

app = App(title="Average Photo Booth",height=880,width=1920)

pic = Picture(app, image="avg.jpg",height=600)
button = PushButton(app, command=both, text="Capture & Recompute")
button2 = PushButton(app, command=recompute_avg, text="recompute")
button3 = PushButton(app, command=capture_image, text="capture")


app.display()
