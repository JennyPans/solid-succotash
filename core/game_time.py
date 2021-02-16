import time


class Time:
    """
    Gère le temps et donne le deltatime
    """

    def __init__(self):
        self.last_time = time.time() * 1000

    def dt(self):
        """
        Calcule le temps entre deux tours de boucle de jeu
        :return: le temps entre deux tours de boucle de jeu
        """
        current_time = time.time() * 1000
        dt = current_time - self.last_time
        self.last_time = current_time
        return dt
