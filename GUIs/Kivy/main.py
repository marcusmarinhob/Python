## @package main.py
# This module creates a GUI based on Kivy Framework.
# 
# This application imports widgets from Kivy Framework.

from kivy.app import App                        # Importing class kivy.app in order to create a new app
from kivy.uix.button import Button              # Importing class kivy.uix.button in order to create a new button object 
from kivy.uix.boxlayout import BoxLayout        # Importing class kivy.uix.boxlayout in order to create a new layout scheme

class Test(App):                                # Creating the class Test inheriting class App properties
    def build(self):                            # New method for the class Test
        box = BoxLayout()                       # Creation of a box layout
        button1 = Button(text='Button1')        # Creation of the Button1
        button2 = Button(text='Button2')        # Creation of the Button2
        box.add_widget(button1)                 # Adding button1 the box 
        box.add_widget(button2)                 # Adding button2 the box 
        return box    

Test().run()                                    # Run the Test app