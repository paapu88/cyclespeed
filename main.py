"""
App for cycling:
upper part of screen you see current velocity (km/h)
lower part you see average velocity (km/h)

Average velocity is updated when speed is > 5 km/h
So rest periods are automatically cut off.
"""

from kivymd.app import MDApp

from kivymd.uix.label import MDLabel

from kivy.uix.gridlayout import GridLayout
from kivy.utils import platform
from plyer import gps
# Request permissions on Android
if platform == 'android':
    from android.permissions import Permission, request_permissions
import numpy as np
from time import sleep

class Grid_LayoutApp(MDApp):
    def __init__(self, min_speed, **kwargs):
        print(min_speed)
        super().__init__(**kwargs)
        self.speeds = []
        self.speed_sum = 0.0
        self.speed_n = 0
        self.average_speed = None
        self.min_speed = min_speed
        self.init =True


    def update_speed(self, lat, lon, speed, bearing, altitude, accuracy):
        """ this is target function defined below (gps.configure(on_location=self.update_speed))
            and based on plyer.gps
        """
        if self.init:
            self.init=False
            sleep(5) # to show initial text
            self.button1.font_style='H1'
            self.button2.font_style='H1'

        speed = speed * 3.6 # m/s -> km/h
        if speed > self.min_speed:
            self.speed_sum += speed
            self.speed_n += 1
            self.average_speed = self.speed_sum/self.speed_n
        self.button1.text = str(int(round(speed)))
        if self.average_speed is not None:
            self.button2.text = str(int(round(self.average_speed)))
        else:
            self.button2.text = "0"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        if platform == 'android':
            request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
        gps.configure(on_location=self.update_speed)
        gps.start(minTime=5000, minDistance=0)
        layout = GridLayout(rows=2)

        # 1st row
        self.button1 = MDLabel(text=f'Speed',halign='center',
                               font_style='Subtitle1', text_color=(0,1,0,1), theme_text_color= "Custom")
        self.button2 = MDLabel(text=f'Average Speed (gathered only when speed > 5km/h)',halign='center',
                               font_style='Subtitle1', text_color=(0,1,0,1), theme_text_color= "Custom")
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)

        # returning the layout
        return layout


# creating object of the App class
root = Grid_LayoutApp(min_speed=5)
# run the App
root.run()


"""

from kivymd.app import MDApp
from plyer import gps


    def print_locations(**kwargs):
        print 'lat: {lat}, lon: {lon}'.format(**kwargs)
        # later
        #gps.stop()

class MainApp(MDApp):

    def update_speed(self, **kwargs):

    def on_start(self):
        gps.configure(on_location=self.update_speed)
        gps.start()

        # Connect to database

MainApp().run()

"""