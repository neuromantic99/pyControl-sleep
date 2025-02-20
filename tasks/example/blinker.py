# A simple state machine which flashes the blue LED on the pyboard on and off.
# Does not require any hardware except micropython board.

from devices.breakout_1_2 import Breakout_1_2
from pyControl.utility import *
from devices import *


import hardware_definition as hw

# Define hardware (normally done in seperate hardware definition file).


# States and events.

orange_LED = hw.orange_LED
blue_LED = hw.green_LED

speaker = hw.speaker

speaker.set_volume(100)


states = [
    "LED_on",
    "LED_off",
]

events = []

initial_state = "LED_off"

# State behaviour functions
board = Breakout_1_2()  # Instantiate the breakout board object.


def LED_on(event):
    if event == "entry":
        timed_goto_state("LED_off", 0.1 * second)
        orange_LED.LED.on()
        blue_LED.LED.on()
        speaker.sine(10)

    elif event == "exit":
        orange_LED.LED.off()
        blue_LED.LED.off()
        speaker.off()


def LED_off(event):
    if event == "entry":
        timed_goto_state("LED_on", 0.1 * second)


# Run end behaviour
