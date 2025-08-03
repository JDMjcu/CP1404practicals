""" 
CP1404 Practical
Box_layout modifications
JDM

"""


from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ An app for greeting the inputted name. """
    
    def build(self):
        """ Build the Kivy app from the kv file. """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self, name):
        """ Greets user (on button press), output result to label widget. """
        try:
            self.root.ids.output_label.text = (f"Hello {name}")
        except ValueError:
            pass
        
    def handle_clear(self):
        """ On button press clear text on label widget. """
        try:
            result = ''
            self.root.ids.output_label.text = result 
        except ValueError:
            pass
        
BoxLayoutDemo().run()