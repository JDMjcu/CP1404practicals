""" 
Dynamic labels Task
Prac 08
JDM

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """An app that creates Labels dynamically from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # The model: a list of names (strings)
        self.name_list = ["Alice", "Bob", "Charlie", "Dana", "Tyrone", "Mahammad", "Jemal"]
        
    def build(self):
        """Build the GUI and create Labels."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name in the list and add to GUI."""
        for name in self.name_list:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)   

DynamicLabelsApp().run()