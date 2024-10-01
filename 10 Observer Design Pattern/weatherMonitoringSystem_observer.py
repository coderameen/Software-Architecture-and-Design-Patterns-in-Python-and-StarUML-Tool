class WeatherStation:
    def __init__(self):
        self.subscribers = []
        self.temperature = 0

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self):
        for sub in self.subscribers:
            sub.update(self.temperature)

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify()

class DisplayDevice:
    def update(self, temp):
        print(f"Temperature updated: {temp}°C")

# Client Code
station = WeatherStation()
display1 = DisplayDevice()
display2 = DisplayDevice()

station.subscribe(display1)
station.subscribe(display2)

station.set_temperature(25)  # Notify displays
