from machine import Pin, UART
import time

COMMAND_PARSE = b'\n'
LOOP_SLEEP = 0.1


class UARTServer:
    buffer: bytes

    command_count = -1

    def __init__(self):
        self.uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
        print(self.uart0)

        self.reset()

    def activate(self):
        while True:
            if self.uart0.any():
                last_bytes: bytes = self.uart0.read()

                while COMMAND_PARSE in last_bytes:
                    index = last_bytes.index(COMMAND_PARSE)
                    self.buffer += last_bytes[:index]
                    self.process()
                    self.reset()
                    last_bytes = last_bytes[index + 1:]

                self.buffer += last_bytes

            time.sleep(LOOP_SLEEP)  # Is this necessary for single threaded server

    def process(self):
        print(self.buffer)

    def reset(self):
        self.buffer = b''
        self.command_count += 1
