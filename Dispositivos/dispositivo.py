from abc import ABC, abstractmethod
from Observer.observer import Observable

class Dispositivo(ABC, Observable):
    def __init__(self, nome, ambiente):
        super().__init__()
        self.nome = nome
        self.ambiente = ambiente
        self.state = 'desligado'

    @abstractmethod
    def status(self):
        pass

    def set_state(self, state):
        self.state = state
        self.notify_observers()