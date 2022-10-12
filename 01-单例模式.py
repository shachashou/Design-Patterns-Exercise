def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class A:
    name = ""

    def __init__(self, name):
        self.name = name
        print(111)

    def __del__(self):
        print(222, self.name)


a = A("A")
print(a.name)
b = A("B")
print(b.name)
c = A("C")
print(c.name)
