import unittest
from Zadanie1.Note import Note

class TestNote(unittest.TestCase):

    def setUp(self):
        self.temp = Note("note", 3)

    def test_ok_name(self):
        self.assertEqual(self.temp.get_name(), "note")

    def test_ok_note(self):
        self.assertEqual(self.temp.get_note(), 3)

    def test_name_null_exception(self):
        with self.assertRaises(Exception):
            n = Note(None, 4)

    def test_note_below_2_exception(self):
        with self.assertRaises(Exception):
            n = Note("note1", 1)

    def test_note_over_6_exception(self):
        with self.assertRaises(Exception):
            n = Note("note1", 7)

    def test_wrong_note_exception(self):
        with self.assertRaises(Exception):
            n = Note("note1", 3.33)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
