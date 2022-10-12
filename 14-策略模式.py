class Strategy:
    def do_algorithm(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


class Context:
    strategy = Strategy()

    def __init__(self, strategy):
        self.strategy = strategy

    def do_some_business_logic(self):
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self.strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


a = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
a.do_some_business_logic()
print()

print("Client: Strategy is set to reverse sorting.")
a.strategy = ConcreteStrategyB()
a.do_some_business_logic()
