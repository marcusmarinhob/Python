## @package main.py
# This module creates a GUI based on Kivy Framework.
# 
# This application imports widgets from Kivy Framework.

from kivy.app import App                            # Importing class kivy.app in order to create a new app
from kivy.uix.button import Button                  # Importing class kivy.uix.button in order to create a new button object 
from kivy.uix.boxlayout import BoxLayout            # Importing class kivy.uix.boxlayout in order to create a new layout scheme
from kivy.uix.label import Label                    # Importing class kivy.uix.label in order to create a new label object 

class Test(App):                                    # Creating the class Test inheriting class App properties
    def build(self):                                # New method for the class Test
        box = BoxLayout(orientation='vertical')     # Creation of a box layout
        
        self.button1 = Button(text='Increment', on_release=self.increment)      # Creation of the Button1
        self.button2 = Button(text='Decrement', on_release=self.decrement)      # Creation of the Button2
        self.label1 = Label(text='0', font_size='50')                           # Creation of the Label1
        
        box.add_widget(self.button1)                     # Adding button1 the box 
        box.add_widget(self.button2)                     # Adding button2 the box 
        box.add_widget(self.label1)                      # Adding button2 the box 

        return box    

    def increment(self, button):
        self.label1.text = str(int(self.label1.text)+1)

    def decrement(self, button):
        self.label1.text = str(int(self.label1.text)-1)



Test().run()    # Run the Test app