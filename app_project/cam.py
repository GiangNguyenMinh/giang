from kivy.app import App
#Use Kivy language
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import cv2

#Call OpenCV
def video():
    cap=cv2.VideoCapture(0)
    while True:
        ret,im=cap.read()
        cv2.imshow("test video",im)
        key=cv2.waitKey(10)
        if key==27:
            break
        if key==" ":
            print("hello")
        return cv2.imshow("test",im)

#Use Kivy language to write interface framework
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: video
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: video.play = not video.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')
#Create a box layout class to implement screenshots
class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['video']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
#Main program
class TestCamera(App):
    def build(self):
        return CameraClick()