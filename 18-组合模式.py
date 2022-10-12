from __future__ import annotations


class Component:
    parent = None

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        return "Leaf"


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)
        component.parent = self

    def remove(self, component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component):
    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1, component2):
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


simple = Leaf()
print("Client: I've got a simple component:")
client_code(simple)
print("\n")

# ...as well as the complex composites.
tree = Composite()

branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

branch2 = Composite()
branch2.add(Leaf())

tree.add(branch1)
tree.add(branch2)

print("Client: Now I've got a composite tree:")
client_code(tree)
print("\n")

print("Client: I don't need to check the components classes even when managing the tree:")
client_code2(tree, simple)

