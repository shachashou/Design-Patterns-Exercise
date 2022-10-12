class Context:
    data = {}
    status = "A"
    state = None

    def __init__(self):
        self.transition_to(self.status)

    def transition_to(self, status):
        print(f"Context: Transition to {status}")
        self.status = status
        if status == "A":
            self.state = ConcreteStateA()
        elif status == "B":
            self.state = ConcreteStateB()
        self.state.context = self

    def request1(self):
        self.state.handle1()

    def request2(self):
        self.state.handle2()


class State:
    context = None

    def handle1(self):
        pass

    def handle2(self):
        pass


class ConcreteStateA(State):
    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to("B")


class ConcreteStateB(State):

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to("A")


a = Context()
a.request1()
a.request2()
