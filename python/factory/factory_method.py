from abc import ABC, abstractmethod
import enum
import random


class XMLParser(ABC):

    @abstractmethod
    def parse():
        print("-- You have not implemented parse method!!.")


class ErrorXMLParser(XMLParser):

    def parse(self):
        print("-- parsing error xml.")


class FeedBackXMLParser(XMLParser):

    def parse(self):
        print("-- parsing feedback xml.")


class OrderXMLParser(XMLParser):

    def parse(self):
        print("-- parsing order xml.")


class ResponseXMLParser(XMLParser):

    def parse(self):
        print("-- parsing response xml.")


class DisplayService(ABC):
    @classmethod
    def display(cls):

        xml_parser = cls.get_parser()
        xml_parser.parse()

    @abstractmethod
    def get_parser():
        print("-- You have not implemented get_parser method")


class XMLErrorDisplayService(DisplayService):

    def get_parser():
        return ErrorXMLParser()


class XMLFeedBackDisplayService(DisplayService):

    def get_parser():
        return FeedBackXMLParser()


class XMLOrderDisplayService(DisplayService):

    def get_parser():
        return OrderXMLParser()


class XMLResponseDisplayService(DisplayService):

    def get_parser():
        return ResponseXMLParser()


class EnumMap(enum.Enum):
    error = XMLErrorDisplayService
    feedback = XMLFeedBackDisplayService
    order = XMLOrderDisplayService
    response = XMLResponseDisplayService


if __name__ == "__main__":
    for enum_iter in EnumMap:
        print(enum_iter.value)

    xml_type = ['order', 'response', 'feedback', 'error']
    for index in range(1, 11):
        xml_parser = EnumMap[random.choice(xml_type)].value()
        xml_parser.display()
