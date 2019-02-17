from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        raise NotImplemented


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def registerObserver(self,observer):
        raise NotImplemented

    @abstractmethod
    def removeObserver(self,observer):
        raise NotImplemented

    @abstractmethod
    def notifyObserver(self):
        raise NotImplemented
