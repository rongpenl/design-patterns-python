class Tuner():
    def __init__(self):
        pass

    def on(self):
        print("Tuner is on.")

    def off(self):
        print("Tuner is off.")


class DVDPlayer():

    def on(self):
        print("DVD is on.")

    def off(self):
        print("DVD is off.")

    def play(self, movie_name: str):
        print("Play {} on DVD.".format(movie_name))


class CDPlayer():

    def on(self):
        print("CD is on.")

    def off(self):
        print("CD is off.")


class Projector():

    def on(self):
        print("Projector is on.")

    def off(self):
        print("Projector is off.")


class Light():

    def on(self):
        print("Light is on.")

    def off(self):
        print("Light is off.")


class Screen():

    def on(self):
        print("Screen is on.")

    def off(self):
        print("Screen is off.")


class PopcornPopper():

    def on(self):
        print("Popcorn Popper is on.")

    def off(self):
        print("Popcorn Popper is off.")


class Amplifier():
    def __init__(self):
        pass

    def on(self):
        print("Amplifier is on.")

    def off(self):
        print("Amplifier is off.")

    def set_tuner(self, tuner: Tuner):
        self.tuner = tuner

    def set_cd(self, cd_player: CDPlayer):
        self.cd_player = cd_player

    def set_dvd(self, dvd_player: DVDPlayer):
        self.dvd_player = dvd_player


class HomeTheater():
    def __init__(self, amp: Amplifier,
                 tuner: Tuner,
                 dvd_player: DVDPlayer,
                 cd_player: CDPlayer,
                 projector: Projector,
                 screen: Screen,
                 light: Light,
                 popcorn_popper: PopcornPopper):
        self.amp = amp
        self.tuner = tuner
        self.dvd_player = dvd_player
        self.cd_player = cd_player
        self.screen = screen
        self.light = light
        self.popcorn_popper = popcorn_popper
        self.amp.set_cd(self.cd_player)
        self.amp.set_dvd(self.dvd_player)
        self.amp.set_tuner(self.tuner)

    def watch_movie(self, movie_name: str):
        print("Prepare to watch {}".format(movie_name))
        self.amp.on()
        self.dvd_player.on()
        self.dvd_player.play(movie_name)

    def end_movie(self):
        pass


if __name__ == "__main__":
    home_theater = HomeTheater(Amplifier(),
                               Tuner(),
                               DVDPlayer(),
                               CDPlayer(),
                               Projector(),
                               Screen(),
                               Light(),
                               PopcornPopper())
    home_theater.watch_movie("Moon river")
