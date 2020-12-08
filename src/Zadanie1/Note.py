
class Note:

    def __init__(self, name, note):
        if name is None or name == "":
            raise Exception("Nazwa nie może być pusta")
        else:
            self.name = name

        if 2 <= note <= 6 and (note * 2) % 2 == 0:
            self.note = note
        else:
            raise Exception("Podaj ocenę od 2 do 6")

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


