## @package main.py
# This module creates a GUI based on Kivy Framework.
# 
# This application imports widgets from Kivy Framework.

from kivy.app import App                            # Importing class kivy.app in order to create a new app
from kivy.uix.boxlayout import BoxLayout            # Importing class kivy.uix.boxlayout in order to create a new layout scheme

class Incrementer(BoxLayout):
    pass

class Test(App):                                    # Creating the class Test inheriting class App properties
    def build(self):                                # New method for the class Test
        return Incrementer()    

Test().run()    # Run the Test app