class TV:
    def on(self): print("TV ON")
    def off(self): print("TV OFF")

class SoundSystem:
    def on(self): print("Sound ON")
    def off(self): print("Sound OFF")

class Lights:
    def dim(self): print("Lights DIM")
    def bright(self): print("Lights BRIGHT")

class HomeTheatreFacade:
    def __init__(self): 
        self.tv = TV()
        self.sound = SoundSystem()
        self.lights = Lights()

    def watch_movie(self):
        self.lights.dim(); self.tv.on(); self.sound.on()

    def end_movie(self):
        self.tv.off(); self.sound.off(); self.lights.bright()

# Client Code
home_theatre = HomeTheatreFacade()
home_theatre.watch_movie()  # Start movie
home_theatre.end_movie()    # End movie
