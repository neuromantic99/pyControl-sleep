# This hardware definition specifies that 3 pokes are plugged into ports 1-3 and a speaker into
# port 4 of breakout board version 1.2.  The houselight is plugged into the center pokes solenoid socket.


from devices.audio_board import Audio_board
from devices.breakout_1_2 import Breakout_1_2
from devices.poke import Poke
from devices.LED_strip import LEDStrip

board = Breakout_1_2()

# Instantiate Devices.
orange_LED = LEDStrip(board.port_1)
blue_LED = LEDStrip(board.port_2)

speaker = Audio_board(board.port_3)
