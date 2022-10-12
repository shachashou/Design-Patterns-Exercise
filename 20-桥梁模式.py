class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        print(f"Abstraction: Base operation with")
        self.implementation.operation_implementation()


class ExtendedAbstraction(Abstraction):
    def operation(self):
        print(f"ExtendedAbstraction: Extended operation with")
        self.implementation.operation_implementation()


class Implementation:
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        print("ConcreteImplementationA: Here's the result on the platform A.")


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        print("ConcreteImplementationB: Here's the result on the platform B.")


a = ConcreteImplementationA()
abstraction = Abstraction(a)
abstraction.operation()

print("\n")

a = ConcreteImplementationB()
abstraction = ExtendedAbstraction(a)
abstraction.operation()
