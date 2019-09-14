## @package main.py
# This module creates a GUI based on Kivy Framework.
# 
# This first application imports the class kivy.app and kivy.uix.button both from Kivy Framework.

from kivy.app import App                        # Importing class kivy.app in order to create a new app
from kivy.uix.button import Button              # Importing class kivy.uix.button in order to create a new button object 

class Test(App):                                # Creating the class Test inheriting class App properties
    def build(self):                            # New method for the class Test
        return Button(text = 'Hello World!')    # Creation of the Button ('Hello World')

Test().run()                                    # Run the Test app