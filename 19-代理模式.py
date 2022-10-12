class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    @staticmethod
    def check_access():
        print("Proxy: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access():
        print("Proxy: Logging the time of request.", end="")


print("Client: Executing the client code with a real subject:")
real_subject = RealSubject()
real_subject.request()

print("")

print("Client: Executing the same client code with a proxy:")
proxy = Proxy(real_subject)
proxy.request()
