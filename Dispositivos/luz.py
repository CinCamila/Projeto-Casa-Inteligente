from transitions import Machine
from Dispositivos.dispositivo import Dispositivo

class Luz(Dispositivo):
    estados = ['desligada', 'ligada']

    def __init__(self, nome, ambiente):
        super().__init__(nome, ambiente)
        self.machine = Machine(model=self, states=self.estados, initial='desligada')
        self.machine.add_transition('ligar', 'desligada', 'ligada', after='notify_observers')
        self.machine.add_transition('desligar', 'ligada', 'desligada', after='notify_observers')

    def status(self):
        return f"Luz {self.nome} está {self.state}"
