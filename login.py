# Creating the login page

# Creating the app
import kivy
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextFieldRound
Factory.register('MDTextFieldRound', module='kivymd.uix.textfield')


class Myapp(MDApp):
    def build(self):
        return
    
Myapp().run()


