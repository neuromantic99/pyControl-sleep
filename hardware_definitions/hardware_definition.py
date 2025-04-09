# This hardware definition specifies that 3 pokes are plugged into ports 1-3 and a speaker into
# port 4 of breakout board version 1.2.  The houselight is plugged into the center pokes solenoid socket.


from devices.audio_board import Audio_board
from devices.breakout_1_2 import Breakout_1_2
from devices.frame_trigger import Frame_trigger
from devices.poke import Poke
from devices.LED_strip import LEDStrip
from pyControl.hardware import Rsync

board = Breakout_1_2()

# Instantiate Devices.
orange_LED = LEDStrip(board.port_3, color='orange')
blue_LED = LEDStrip(board.port_2, color='blue')

speaker = Audio_board(board.port_4)
frame_trigger = Frame_trigger(pin=board.BNC_1, pulse_rate=30) 
sync_output = Rsync(pin=board.BNC_2, mean_IPI=1000) # Instantiate Rsync object on breakout board BNC_1
print(sync_output)