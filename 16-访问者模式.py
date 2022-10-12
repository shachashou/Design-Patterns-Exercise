from __future__ import annotations


class Component:
    def accept(self, visitor):
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_a(self)

    @staticmethod
    def exclusive_method_of_concrete_component_a():
        return "A"


class ConcreteComponentB(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_b(self)

    @staticmethod
    def special_method_of_concrete_component_b():
        return "B"


class Visitor:
    def visit_concrete_component_a(self, element):
        pass

    def visit_concrete_component_b(self, element):
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


components = [ConcreteComponentA(), ConcreteComponentB()]

print("The client code works with all visitors via the base Visitor interface:")
visitor1 = ConcreteVisitor1()
for component in components:
    component.accept(visitor1)

print("It allows the same client code to work with different types of visitors:")
visitor2 = ConcreteVisitor2()
for component in components:
    component.accept(visitor2)
