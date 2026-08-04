from abc import ABC, abstractmethod

class ResponseValidator(ABC):

    @abstractmethod
    def validate(self,data):
        pass