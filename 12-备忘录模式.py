from __future__ import annotations

from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    _state = None

    def __init__(self, state):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self):
        print("Originator: I'm doing something important.")
        self._state = "".join(sample(ascii_letters, 30))
        print(f"Originator: and my state has changed to: {self._state}")

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento:
    def get_name(self):
        pass

    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self):
        return self._date


class Caretaker:
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


a = Originator("Super-duper-super-puper-super.")
b = Caretaker(a)

b.backup()
a.do_something()

b.backup()
a.do_something()

b.backup()
a.do_something()

print()
b.show_history()

print("\nClient: Now, let's rollback!\n")
b.undo()

print("\nClient: Once more!\n")
b.undo()
print("\nClient: Once more!\n")
b.undo()
