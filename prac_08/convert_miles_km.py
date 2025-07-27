"""
CP1404 Practical
Kivy GUI square a number task

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILESINKILOMETER = 1.609344 # 1 Mile = 1.609344 Kilometers

class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to kilometers """
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ Converts Miles to kilometes when button is pressed, output result to label widget. """
        try:
            result = float(value) * MILESINKILOMETER
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass
    
    def handle_increment(self, value, direction):
        try:
            number = float(value) + direction
            self.root.ids.input_number.text = str(number)
        except ValueError:
            pass

ConvertMilesApp().run()