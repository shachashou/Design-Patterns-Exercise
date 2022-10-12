class ABSTRACT_ITERATOR:
    def first(self):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def is_done(self):
        raise NotImplementedError()

    def current_item(self):
        raise NotImplementedError()


class CONCRETE_ITERATOR(ABSTRACT_ITERATOR):
    index = 0
    data = []

    def __init__(self, data):
        self.data = data

    def first(self):
        self.index = 0

    def next(self):
        if self.index + 1 < len(self.data):
            self.index += 1
        else:
            self.index = 0

    def is_done(self):
        if self.index + 1 == len(self.data):
            return True
        else:
            return False

    def current_item(self):
        return self.data[self.index]


class ABSTRACT_AGGRATE:
    data = []

    def create_iterator(self):
        raise NotImplementedError()


class CONCRETE_AGGRATE(ABSTRACT_AGGRATE):
    data = [x for x in range(10)]

    def create_iterator(self):
        return CONCRETE_ITERATOR(self.data)


a = CONCRETE_AGGRATE()
b = a.create_iterator()
b.first()
while not b.is_done():
    print(b.current_item())
    b.next()
