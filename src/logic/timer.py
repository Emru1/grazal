from pygame import time


class Timer:
    """
    Klasa Timera, odmierza czas i odpala poszczególne instancje po przekroczeniu odstępu czasowego
    """

    class Action:
        def __init__(self, interval, instance):
            self.last_run = time.get_ticks()
            self.interval = interval
            self.instance = instance

    def __init__(self):
        self.time = time.get_ticks()
        self.actions = []

    def run(self):
        """
        Sprawdza i odpala poszczegolne obiekty z metodami timer_run
        :rtype: object
        """
        self.time = time.get_ticks()
        for action in self.actions:
            if action.last_run + action.interval <= self.time:
                action.last_run = self.time
                action.instance.timer_run()

    def add(self, interval, instance):
        """
        Dodaje nowe zadanie z zadanym interwałem i obiektem
        obiekt musi posiadać metodę timer_run
        :rtype: object
        :param interval: int
        :param instance: Klasa z metodą timer_run
        """
        if "timer_run" not in dir(instance):
            log.log("Obiekt " + str(instance) + ", " + instance.__name__ + " nie posiada metody timer_run()")
        else:
            act = self.Action(interval, instance)
            self.actions.append(act)
