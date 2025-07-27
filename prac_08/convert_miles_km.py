"""
CP1404 Practical
Kivy GUI square a number task

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_IN_KILOMETER  = 1.609344 # 1 Mile = 1.609344 Kilometers

class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to kilometers """
    output_text = StringProperty('')  # Initial value
    
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ Converts Miles to kilometes when button is pressed, output result to label widget. """
        try:
            result = float(value) * MILES_IN_KILOMETER
            self.output_text = str(result)
        except (ValueError, TypeError):
            self.output_text = "0.0"  
            
    def handle_increment(self, value, direction):
        try:
            number = float(value) + direction
            self.root.ids.input_number.text = str(number)
        except ValueError:
            pass

ConvertMilesApp().run()