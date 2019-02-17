from observer import *
import sys


class Display:
    def __init__(self, state):
        self.value = state

    def display(self):
        print(self.value)


class CurrentConditionsDisplay(Display, Observer):
    def __init__(self, start_value=None):
        super(CurrentConditionsDisplay, self).__init__(start_value)

    def update(self, state):
        self.value = state
        self.display()


class StatisticDisplay(Display, Observer):
    def __init__(self, state=None):
        if state is None:
            state = []
        super(StatisticDisplay, self).__init__(state)

    def update(self, state):
        self.value.append(state)
        self.display()


class Station(Subject):
    def __init__(self):
        self.observers = set()
        self.value = None

    def registerObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.value)

    def stateChanged(self):
        self.notifyObserver()

    def setValue(self, state):
        self.value = state
        self.stateChanged()


if __name__ == "__main__":
    display1 = StatisticDisplay()
    display2 = CurrentConditionsDisplay()

    st = Station()
    st.registerObserver(display1)
    st.registerObserver(display2)
    for i in range(5):
        value = input()
        st.setValue(value)
