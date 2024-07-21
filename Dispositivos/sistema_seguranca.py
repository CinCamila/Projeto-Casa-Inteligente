from transitions import Machine
from Dispositivos.dispositivo import Dispositivo

class SistemaSeguranca(Dispositivo):
    estados = ['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa']

    def __init__(self, nome, ambiente):
        super().__init__(nome, ambiente)
        self.machine = Machine(model=self, states=self.estados, initial='desarmado')
        self.machine.add_transition('armar_com_gente_em_casa', 'desarmado', 'armado_com_gente_em_casa', after='notify_observers')
        self.machine.add_transition('armar_sem_gente_em_casa', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa', after='notify_observers')
        self.machine.add_transition('desarmar', '*', 'desarmado', after='notify_observers')

    def status(self):
        estadoEdit = f"{self.state.replace('_', ' ')}"
        return f"Sistema de Segurança {self.nome} está {estadoEdit}"

