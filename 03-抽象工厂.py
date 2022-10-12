class TechnicalBook:
    @staticmethod
    def publish():
        print("Python-Book")


class LiteraryBooks:
    @staticmethod
    def publish():
        print("Black Hole Book")


class FACTORY:
    @staticmethod
    def publish_book():
        return None


class TechnicalFactory(FACTORY):
    @staticmethod
    def publish_book():
        return TechnicalBook()


class LiteraryFactory(FACTORY):
    @staticmethod
    def publish_book():
        return LiteraryBooks()


a = TechnicalFactory.publish_book()
a.publish()
b = LiteraryFactory.publish_book()
b.publish()
