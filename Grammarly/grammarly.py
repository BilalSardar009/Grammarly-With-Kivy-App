
import os
os.environ["KIVY_NO_CONSOLELOG"]="1"
from unittest import TextTestResult
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from matplotlib.pyplot import title
from numpy import source
import random
from gingerit.gingerit import GingerIt

class CorrectionApp(MDApp):
    
    #correct
    def correct(self,args):
        try:
          text = self.input.text
          parser = GingerIt()
          print(parser.parse(text)["result"])
          self.corrected.text=parser.parse(text)["result"]
          self.label.text="Correct Sentence is:"
        except ValueError:
          self.label.text="Wrong Input"     
    #flip 
    def flip(self):
        themes=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette=themes[random.randint(0,17)]
        print("Theme Changed")
        
    #build
    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        self.toolbar=MDToolbar(title="Bilal's Grammarly")
        self.toolbar.pos_hint={"top":1}
        self.toolbar.right_action_items=[
        ["rotate-3d-variant",lambda x:self.flip()]]
        screen.add_widget(self.toolbar)
        
        
        #logo
        
        screen.add_widget(Image(
            source="logo.png",
            pos_hint={"center_x":0.5 ,"center_y":0.7}))
        
        
        #input
        
        self.input=MDTextField(
            text="Enter Sentence",
            halign="center",
            size_hint=(0.8,1),
            pos_hint={"center_x":0.5 ,"center_y":0.5},
            font_size=22
        )
        
        screen.add_widget(self.input)
        
        #labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.corrected = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.corrected)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CORRECTION",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            on_press = self.correct
        ))

        
        return screen
    

if __name__ == '__main__':
    CorrectionApp().run()