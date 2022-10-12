class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    @staticmethod
    def base_operation1():
        print("AbstractClass says: I am doing the bulk of the work")

    @staticmethod
    def base_operation2():
        print("AbstractClass says: But I let subclasses override some operations")

    @staticmethod
    def base_operation3():
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    def required_operations1(self):
        pass

    def required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self):
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self):
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self):
        print("ConcreteClass2 says: Overridden Hook1")


a = ConcreteClass1()
a.template_method()
print("#########")
b = ConcreteClass2()
b.template_method()
