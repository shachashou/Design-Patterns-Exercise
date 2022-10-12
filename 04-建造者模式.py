import time


class Pizza:
    name = ""
    dough = None
    sauce = None
    toppings = []

    def __init__(self, name):
        self.name = name

    def prepare_dough(self, dough):
        self.dough = dough
        print(self.dough)
        print('preparing the %s dough of your %s...' % (self.dough, self.name))
        time.sleep(3)
        print('Done with the %s dough' % self.dough)


class PizzaBuilder(object):
    name = None
    pizza = None

    def __init__(self):
        self.progress = 0
        self.baking_time = 5
        self.pizza = Pizza(self.name)

    def prepare_dough(self):
        raise NotImplementedError()

    def add_sauce(self):
        raise NotImplementedError()

    def add_topping(self):
        raise NotImplementedError()

    def bake(self):
        raise NotImplementedError()

    def cut(self):
        raise NotImplementedError()

    def box(self):
        raise NotImplementedError()


class NYStyleCheeseBuilder(PizzaBuilder):
    name = 'NY Style Sauce and Cheese Pizza'

    def prepare_dough(self):
        self.progress = 0
        self.pizza.prepare_dough('thin')

    def add_sauce(self):
        print('adding the tomato sauce to your pizza..')
        self.pizza.sauce = 'tomato'
        time.sleep(1)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (grated reggiano cheese) to your pizza')
        self.pizza.toppings.append(["Grated", "Reggiano", "Cheese"])
        time.sleep(1)
        print('done with the topping (grated reggiano cheese)')

    def bake(self):
        self.progress = 1
        print('baking your pizza for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)

    def cut(self):
        self.progress = 2
        print("Cutting the pizza into diagonal slices")

    def box(self):
        self.progress = 3
        print("Place pizza in official PizzaStore box")


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()
        self.builder.bake()
        self.builder.cut()
        self.builder.box()

    @property
    def pizza(self):
        return self.builder.pizza


a = Waiter()
a.construct_pizza(NYStyleCheeseBuilder())
print(a.pizza.name, a.pizza.sauce, a.pizza.toppings)
