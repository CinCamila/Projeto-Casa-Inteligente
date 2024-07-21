from Dispositivos.luz import Luz
from Dispositivos.termostato import Termostato
from Dispositivos.sistema_seguranca import SistemaSeguranca

class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo, nome, ambiente):
        if tipo == 'luz':
            return Luz(nome, ambiente)
        elif tipo == 'termostato':
            return Termostato(nome, ambiente)
        elif tipo == 'sistema_seguranca':
            return SistemaSeguranca(nome, ambiente)
        else:
            raise ValueError(f"Tipo de dispositivo desconhecido: {tipo}")

