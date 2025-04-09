from devices.breakout_1_2 import Breakout_1_2
from devices.LED_strip import LEDStrip
from devices.frame_trigger import Frame_trigger
from pyControl.utility import timed_goto_state, second, withprob, v, print, goto_state

import hardware_definition as hw


orange_LED = hw.orange_LED
blue_LED = hw.blue_LED

speaker = hw.speaker


states = [
    "LED_on",
    "sound_on",
    "inter_stimulus_interval",
    "trial_start",
]

events = ["rsync"]

initial_state = "trial_start"


# State behaviour functions

board = Breakout_1_2()


v.INTER_TRIAL_INTERVAL = 10 * second
v.INTER_STIMULUS_INTERVAL = 1 * second
v.SOUND_LENGTH = 0.5 * second
v.LIGHT_ON_TIME = 0.5 * second

v.previous_conditions = []
v.condition = None


# 40 db 3 - 48 kHz
# 70 db?


# 10 and 30
def trial_start(event: str) -> None:
    if event == "entry":
        v.condition = 0 if withprob(0.5) else 1
        if v.previous_conditions[-3:] == [v.condition] * 3:
            print("Switching condition to prevent 4 in a row")
            v.condition = int(not (v.condition))
        v.previous_conditions.append(v.condition)
        print(f"Starting trial with condition {v.condition}")
        timed_goto_state("LED_on", v.INTER_TRIAL_INTERVAL)


def LED_on(event: str) -> None:
    if event == "entry":
        led = hw.blue_LED if v.condition == 0 else hw.orange_LED
        print(f"Turning on LED {led}")
        led.LED.on()
        timed_goto_state("inter_stimulus_interval", v.LIGHT_ON_TIME)

    elif event == "exit":
        led = hw.blue_LED if v.condition == 0 else hw.orange_LED
        led.LED.off()


def inter_stimulus_interval(event: str) -> None:
    if event == "entry":
        timed_goto_state("sound_on", v.INTER_STIMULUS_INTERVAL)


def sound_on(event: str) -> None:
    if event == "entry":
        if v.condition == 0:
            sound_frequency = 6000
            speaker.set_volume(10)
        else:
            sound_frequency = 14000
            speaker.set_volume(70)

        speaker.sine(sound_frequency)
        print(f"Deliverying sound frequency {sound_frequency}")
        timed_goto_state("trial_start", v.SOUND_LENGTH)
    elif event == "exit":
        speaker.off()


def run_end() -> None:  # Turn off hardware at end of run.
    blue_LED.LED.off()
    orange_LED.LED.off()
    speaker.off()
