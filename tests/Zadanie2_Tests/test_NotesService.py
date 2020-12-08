import unittest
from Zadanie2.NotesService import NotesService
from Zadanie2.NotesStorage import NotesStorage
from Zadanie1.Note import Note
from unittest.mock import *

class TestNotesService(unittest.TestCase):

    def test_add(self):
        # prepare mock
        test_object = NotesStorage()
        test_object.add = Mock(name='add')
        test_object.add.return_value = Note('note', 3)

        notes_service = NotesService(test_object)
        self.assertIsInstance(notes_service.add(Note('note', 3)), Note)

    def test_clear(self):
        test_object = NotesStorage()
        test_object.clear = Mock(name='clear')
        test_object.return_value = [Note('note', 3)]

        notes_service = NotesService(test_object)
        notes_service.clear()
        test_object.return_value = []

        self.assertEqual(notes_service.storage.getAllNotesOf('note'), [])


if __name__ == '__main__':
    unittest.main()