from serial import Serial


SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_BAUD = 9600


class UARTClient:
    def __init__(self, port: str = None, baud: int = None):
        self.serial = Serial(port or SERIAL_PORT, baudrate=baud or SERIAL_BAUD)

    def __del__(self):
        self.serial.close()

    def send(self, data: bytes):
        self.serial.write(data)


if __name__ == '__main__':
    client = UARTClient()
    client.send(b'StepperMotor01|+|1|Response00\n')
