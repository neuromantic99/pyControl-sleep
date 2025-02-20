from pyControl.hardware import Digital_output, Digital_input


class LEDStrip:

    def __init__(self, port, rising_event=None, falling_event=None, debounce=5):
        self.input = Digital_input(port.DIO_A, rising_event, falling_event, debounce)
        self.LED = Digital_output(port.POW_B)
        if port.POW_C is not None:
            self.POW_C = Digital_output(port.POW_C)

    def value(self):
        return self.input.value()
