from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.lang import Builder
import numpy as np
import cv2

Builder.load_file("kivy_layout.kv")
class AndroidCamera(Camera):
    camera_resolution = (640, 480)
    counter = 0
    def _camera_off(self, *largs):
        self.texture = None
    def _camera_loaded(self, *largs):
        self.texture = Texture.create(size=np.flip(self.camera_resolution), colorfmt='rgb')
        self.texture_size = list(self.texture.size)

    def on_tex(self, *l):
        if self._camera._buffer is None:
            return None
        frame = self.frame_from_buf()
        self.frame_to_screen(frame)
        super(AndroidCamera, self).on_tex(*l)

    def frame_from_buf(self):
        w, h = self.resolution
        frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
        frame_bgr = cv2.cvtColor(frame, 93)
        return np.rot90(frame_bgr, 3)

    def frame_to_screen(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_hsv = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2HSV)
        low_orange = np.array([10, 100, 20])
        heigh_orange = np.array([25, 255, 255])
        mask = cv2.inRange(frame_hsv, low_orange, heigh_orange)
        screen_frame = cv2.bitwise_and(frame_rgb, frame_rgb, mask=mask)
        cv2.putText(screen_frame, str(self.counter), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        self.counter += 1
        flipped = np.flip(screen_frame, 0)
        buf = flipped.tostring()
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera_inside = BoxLayout()
        self.add_widget(self.camera_inside)

        # camera

        self.Android = AndroidCamera()
        self.Android.index = 0
        self.Android.play = False
        self.Android.allow_stretch = True
        self.Android.resolution = self.Android.camera_resolution
        self.camera_inside.add_widget(self.Android)

        # BoxLayout Button

        # self.inside = BoxLayout()
        # self.inside.orientation = 'horizontal'
        # self.inside.size_hint = (1, 0.1)
        # self.add_widget(self.inside)

        # Start_Button

        # self.start_button = Button()
        # self.start_button.text = 'Start'
        # self.start_button.bind(on_press=self.start_cam)
        # self.inside.add_widget(self.start_button)

        # Stop_Button

        # self.stop_button = Button()
        # self.stop_button.text = 'Stop'
        # self.stop_button.bind(on_press=self.stop_cam)
        # self.inside.add_widget(self.stop_button)

        self.swap = Button()
        self.swap.text = 'swap'
        self.swap.bind(on_press=self.switch_button)
        self.add_widget(self.swap)
    def switch_button(self, instance):
        self.Android.play = not self.Android.play

#
#     def start_cam(self, instance):
#         self.Android.play = True
#         self.Android._camera_loaded()
#     def stop_cam(self, instance):
#         self.Android._camera_off()
#
# #
#
#
class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()