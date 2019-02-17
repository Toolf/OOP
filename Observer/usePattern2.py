from collections.abc import Iterable


class Cell:  # at the same time acts as Observer and Subject
    def __init__(self, dependence, func=None):
        self.observers = set()

        if func is None:
            self.func = lambda *args: args[0] if len(args) == 1 else list(args)
        else:
            self.func = func
        if not isinstance(dependence, Iterable):
            self.dependence = [dependence]
        else:
            self.dependence = dependence

        for observer in self.dependence:
            if isinstance(observer, Cell):
                observer.registerObserver(self)
        self.value = self.func(*self.dependence)

    def update(self):
        self.value = self.func(*self.dependence)
        self.stateChanged()

    def set_value(self, value):
        self.value = value
        self.stateChanged()

    def registerObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update()

    def stateChanged(self):
        self.notifyObserver()


a = Cell(1, lambda x: x+1)
b = Cell(3)
c = Cell([a, b, b], lambda a_local, b_local, c_local: a_local.value + b_local.value + b_local.value)

print(c.value)
a.set_value(7)
print(c.value)
