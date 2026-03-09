class Projector:
    def on(self) -> None:
        print('Projector: Projector is on')

    def set_input(self, source: str) -> None:
        print(f'Projector: The source is set on {source}')

    def off(self) -> None:
        print('Projector: Projector is off')

class SoundSystem:
    def on(self) -> None:
        print('Sound system: The sound system is on')

    def set_volume(self, volume: int) -> None:
        print(f'Sound system: The volume is set on {volume}')


    def off(self) -> None:
        print('Sound system: The sound system  is off')

class DVDPlayer:
    def on(self) -> None:
        print('DVD player: The DVD player is on')

    def play(self, movie: str) -> None:
        print(f'DVD player: The movie called {movie} is running')


    def off(self) -> None:
        print('DVD player: The DVD player  is off')

#FACADE PATTERN INTERFACE
class HomeTheatreFacade:
    def __init__(self) -> None:
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.dvd_player = DVDPlayer()

    def watch_movie(self,
                    source: str,
                    volume: int,
                    movie: str):
        print("/n The home theatre is running:")
        self.projector.on()
        self.projector.set_input(source=source)
        self.sound_system.on()
        self.sound_system.set_volume(volume=volume)
        self.dvd_player.on()
        self.dvd_player.play(movie=movie)

    def off_movie(self) -> None:
        print("/n The home theatre is off:")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()

home_theatre = HomeTheatreFacade()

home_theatre.watch_movie(source="DVD",
                         volume=50,
                         movie="Interstellar")
home_theatre.off_movie()