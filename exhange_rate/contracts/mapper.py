from abc import ABC, abstractmethod

class ResponseMapper(ABC):

    @abstractmethod
    def transform(self, data):
        pass