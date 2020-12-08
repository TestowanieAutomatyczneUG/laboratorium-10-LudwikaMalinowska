
from Zadanie2.NotesStorage import NotesStorage
import math
import statistics

class NotesService:

    def __init__(self, storage):
        self.storage = storage

    def add(self, note):
        return self.storage.add(note)

    def averageOf(self, name):
        grades = self.storage.getAllNotesOf(name)
        grades_mean = statistics.mean(grades)
        return grades_mean

    def clear(self):
        self.storage.clear()
