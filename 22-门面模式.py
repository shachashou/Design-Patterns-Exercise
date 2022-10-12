class Facade:
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        results = [
            "Facade initializes subsystems:",
            self._subsystem1.operation1(),
            self._subsystem2.operation1(),
            "Facade orders subsystems to perform the action:",
            self._subsystem1.operation_n(),
            self._subsystem2.operation_z()
        ]
        return "\n".join(results)


class Subsystem1:

    @staticmethod
    def operation1():
        return "Subsystem1: Ready!"

    @staticmethod
    def operation_n():
        return "Subsystem1: Go!"


class Subsystem2:
    @staticmethod
    def operation1():
        return "Subsystem2: Get ready!"

    @staticmethod
    def operation_z():
        return "Subsystem2: Fire!"


a = Subsystem1()
b = Subsystem2()
facade = Facade(a, b)
facade.operation()
