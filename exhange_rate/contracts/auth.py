from abc import ABC, abstractmethod

class AuthStrategy(ABC):

    @abstractmethod
    def apply(self, request_config):
        pass