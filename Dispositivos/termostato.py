from transitions import Machine
from Dispositivos.dispositivo import Dispositivo

class Termostato(Dispositivo):
    estados = ['desligado', 'aquecendo', 'esfriando']

    def __init__(self, nome, ambiente):
        super().__init__(nome, ambiente)
        self.machine = Machine(model=self, states=self.estados, initial='desligado')
        self.machine.add_transition('aquecer', 'desligado', 'aquecendo', after='notify_observers')
        self.machine.add_transition('esfriar', 'aquecendo', 'esfriando', after='notify_observers')
        self.machine.add_transition('desligar', '*', 'desligado', after='notify_observers')

    def status(self):
        return f"Termostato {self.nome} está {self.state}"


