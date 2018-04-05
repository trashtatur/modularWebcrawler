from abc import ABCMeta, abstractmethod


class Starter(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass
