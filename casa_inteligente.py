from functools import reduce
from Dispositivos.dispositivo import Dispositivo

class CasaInteligente:
    _instance = None

    def __new__(cls, max_dispositivos=5):
        if cls._instance is None:
            cls._instance = super(CasaInteligente, cls).__new__(cls)
            cls._instance.ambientes = {}
            cls._instance.max_dispositivos = max_dispositivos
            cls._instance.total_dispositivos = 0
        return cls._instance

    def adicionar_dispositivo(self, dispositivo):
        if self.total_dispositivos >= self.max_dispositivos:
            print(f"Não é possível adicionar mais dispositivos. Limite de {self.max_dispositivos} dispositivos atingido.")
            return
        ambiente = dispositivo.ambiente
        if ambiente not in self.ambientes:
            self.ambientes[ambiente] = []
        self.ambientes[ambiente].append(dispositivo)
        self.total_dispositivos += 1

def obter_status_dispositivos(ambientes):
    def status_dispositivo(dispositivo):
        return dispositivo.status()

    def status_ambiente(ambiente, dispositivos):
        return [f"Ambiente: {ambiente}"] + list(map(status_dispositivo, dispositivos))

    return [status for ambiente, dispositivos in ambientes.items()
            for status in status_ambiente(ambiente, dispositivos)]

def dispositivos_desligados(ambientes):
    desligados = []
    for ambiente, dispositivos in ambientes.items():
        desligados.extend(filter(lambda d: d.state == 'desligada' or d.state == 'desarmado' or d.state == 'desligado', dispositivos))
    return desligados

def contar_dispositivos_ligados(ambientes):
    dispositivos = [dispositivo for dispositivos in ambientes.values() for dispositivo in dispositivos]
    return reduce(lambda count, d: count + 1 if d.state != 'desligada' or d.state!= 'desligado' or 'desarmado' else count, dispositivos, 0)
