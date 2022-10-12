class TechnicalBooks:
    @staticmethod
    def publish():
        print("Python-Book")


class LiteraryBooks:
    @staticmethod
    def publish():
        print("Black Hole Book")


class SimpleFactory:
    @staticmethod
    def publish_book(name):
        if name == 'technical':
            return TechnicalBooks()
        elif name == 'literary':
            return LiteraryBooks()


techbook = SimpleFactory.publish_book("technical")
literbook = SimpleFactory.publish_book("literary")
