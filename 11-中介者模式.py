class Mediator:
    def notify(self, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    mediator = Mediator()


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify("A")

    def do_b(self):
        print("Component 1 does B.")
        self.mediator.notify("B")


class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")
        self.mediator.notify("C")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify("D")


c1 = Component1()
c2 = Component2()
ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\n", end="")

print("Client triggers operation D.")
c2.do_d()
