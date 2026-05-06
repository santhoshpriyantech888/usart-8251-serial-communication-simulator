class USART8251:
    def __init__(self):
        self.data_buffer = ""
        self.mode = "Asynchronous"
        self.parity = "None"
        self.stop_bits = 1

    def configure(self, mode, parity, stop_bits):
        self.mode = mode
        self.parity = parity
        self.stop_bits = stop_bits
        print(f"Configured: Mode={mode}, Parity={parity}, Stop Bits={stop_bits}")

    def transmit(self, data):
        print(f"Transmitting: {data}")
        self.data_buffer = data

    def receive(self):
        print(f"Receiving: {self.data_buffer}")
        return self.data_buffer


# Simulation
usart = USART8251()

usart.configure("Asynchronous", "None", 1)

data = input("Enter data to transmit: ")
usart.transmit(data)

received = usart.receive()
print("Data Received:", received)
