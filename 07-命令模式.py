class Receiver:
    @staticmethod
    def action1():
        print('Execute action1...')

    @staticmethod
    def action2():
        print('Execute action2...')


class Command:
    def execute(self):
        pass


class Action1(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action1()


class Action2(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action2()


class Invoker:
    actions = []

    def execute(self, action):
        self.actions.append(action)
        action.execute()


a = Receiver()
action1 = Action1(a)
action2 = Action2(a)

b = Invoker()
b.execute(action1)
b.execute(action2)
print(b.actions)
