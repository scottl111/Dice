#!/usr/bin/env python
""" 
For when the kids have lost the Monopoly dice and you want nothing more than to dominate 
London's real estate on a Saturday night. And Sunday night. And maybe Monday. Monopoly is one
hell of a long game. 
"""
import random
from tkinter import *

__author__ = "Scott Lockett"

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Scott Lockett"
__email__ = "scottlockett1994@gmail.com"

"""
Class for the dice GUI
"""
class UserInterface:

    """
    Sets up the GUI window of the application
    """
    def __init__(self):
        self.window = Tk()
        self.window.title("Scott's Dice")
        self.window.geometry('350x200')
        self.number_label = Label(self.window, text=str(self.get_random_dice_number()))

    """
    Adds the number label and 
    """
    def create_UI(self):
        self.number_label.grid(column=0, row=0)
        random_number_button = Button(self.window, text="Roll...", command=self.button_clicked)
        random_number_button.grid(column=1, row=0)
        self.window.mainloop()

    """
    Handles the roll button being clicked
    """
    def button_clicked(self):
        self.number_label.configure(text=self.get_random_dice_number())

    """
    Creates the random dice number
    """
    def get_random_dice_number(self):
        return random.randint(1,6)

def main():
   ui = UserInterface()
   ui.create_UI()
    
if __name__ == "__main__": main()
