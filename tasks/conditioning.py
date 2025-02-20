from devices.breakout_1_2 import Breakout_1_2
from devices.LED_strip import LEDStrip
from pyControl.utility import timed_goto_state, second, withprob, v

import hardware_definition as hw


states = [
    "LED_on",
    "sound_on",
    "inter_stimulus_interval",
    "trial_start",
]

events = []

initial_state = "trial_start"


# State behaviour functions

board = Breakout_1_2()


v.INTER_TRIAL_INTERVAL = 10 * second
v.INTER_STIMULUS_INTERVAL = 0.5 * second
v.SOUND_LENGTH = 0.5 * second
v.LIGHT_ON_TIME = 0.5 * second

v.condition = None


def trial_start(event: str) -> None:
    if event == "entry":
        v.condition = 0 if withprob(0.5) else 1
        print(f"Condition: {v.condition}")
        timed_goto_state("sound_on", v.INTER_TRIAL_INTERVAL)


def sound_on(event: str) -> None:
    if event == "entry":
        sound_frequency = 10000 if v.condition == 0 else 2000
        # audio_output.sound(
        #     sound_frequency
        # )
        timed_goto_state("inter_stimulus_interval", v.SOUND_LENGTH)
    elif event == "exit":
        # audio_output.stop()
        pass


def inter_stimulus_interval(event: str) -> None:
    if event == "entry":
        timed_goto_state("LED_on", v.INTER_STIMULUS_INTERVAL)


def LED_on(event: str) -> None:
    if event == "entry":
        led = hw.green_LED if v.condition == 0 else hw.orange_LED
        led.LED.on()
        timed_goto_state("trial_start", v.INTER_STIMULUS_INTERVAL)

    elif event == "exit":
        led = hw.green_LED if v.condition == 0 else hw.orange_LED
        led.LED.off()


# Run end behaviour


def run_end():  # Turn off hardware at end of run.
    blue_LED.off()
