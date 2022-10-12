# 用到多继承，跳过此节
# class Target:
#     def request(self):
#         return "Target: The default target's behavior."
#
#
# class Adaptee:
#     @staticmethod
#     def specific_request():
#         return ".eetpadA eht fo roivaheb laicepS"
#
#
# class Adapter(Target, Adaptee):
#     def request(self):
#         return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
#
#
# print("Client: I can work just fine with the Target objects:")
# target = Target()
# target.request()
#
# a = Adaptee()
# print("Client: The Adaptee class has a weird interface. "
#       "See, I don't understand it:")
# print(f"Adaptee: {a.specific_request()}", end="\n\n")
#
# print("Client: But I can work with it via the Adapter:")
# adapter = Adapter()
# target.request()
