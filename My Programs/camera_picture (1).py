#camera_picture.py
from picamera import PiCamera
from time import sleep

def main():
    camera = None
    try:
        camera = PiCamera()
        camera.start_preview(fullscreen=False,window=(100,20,640,480)) #(x,y,width,height)
        # Ctrl+D to exit preview
        camera.rotation = 0 # 180
        camera.resolution = (1920,1080)
        camera.image_effect="cartoon"
        camera.annotate_text = "Kyle Moore"
        sleep(4)
        camera.capture("/home/pi/Desktop/image.jpg")
        camera.start_recording("/home/pi/Desktop/videopiclass.h264")
        sleep(4)
        camera.stop_recording()     
    except Exception as e:
        print("Camera not detected or incorrect settings " + str(e))
    finally:
        if camera is not None:
            camera.stop_preview()
            camera.close()
main()
