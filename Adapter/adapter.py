from abc import ABCMeta, abstractmethod


class Interface(metaclass=ABCMeta):
    @abstractmethod
    def change(self, value):
        raise NotImplemented

    @abstractmethod
    def get(self):
        raise NotImplemented


class A:  # Don't use Interface
    def __init__(self, value=0):
        self.value = value

    def changeValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


class B(Interface):
    def __init__(self, value=0):
        self.value = value

    def change(self, value):
        self.value = value + 1

    def get(self):
        return self.value


class C(Interface):
    def __init__(self, value=0):
        self.value = value

    def change(self, value):
        self.value = value - 3

    def get(self):
        return self.value


class AdapterA(A, Interface):  # Adapted class A to Interface
    def change(self, value):
        self.changeValue(value)

    def get(self):
        return self.value


if __name__ == "__main__":
    # [0, 1 , -3]
    arr = [AdapterA(), B(), C()]

    # result -> [1, 2, -2]
    for el in arr:
        el.change(1)

    for el in arr:
        print(el.get())
