from django.db import models


class Process:
    def __init__(self, id, arrival, duration, priority):
        self.id = id
        self.arrival = arrival
        self.duration = duration
        self.priority = priority

        self.remaining = duration
        self.start = None
        self.finish = None
