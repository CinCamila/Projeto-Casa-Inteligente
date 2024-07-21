import argparse
from casa_inteligente import CasaInteligente, obter_status_dispositivos, dispositivos_desligados, contar_dispositivos_ligados
from Dispositivos.dispositivo_factory import DispositivoFactory
from Dispositivos.luz import Luz
from Dispositivos.termostato import Termostato
from Dispositivos.sistema_seguranca import SistemaSeguranca

def main():
    parser = argparse.ArgumentParser(description='Sistema de Casa Inteligente')
    parser.add_argument('--max_dispositivos', type=int, default=5, help='Número máximo de dispositivos')
    args = parser.parse_args()

    casa = CasaInteligente()

    continuar = True

    print("\n\t\tSistema Casa Inteligente\n")

    while continuar:
        print("Menu Principal:")
        print("1. Adicionar dispositivo\n"
              "2. Ver status dos dispositivos\n"
              "3. Ligar luz\n"
              "4. Desligar luz\n"
              "5. Aquecer termostato\n"
              "6. Esfriar termostato\n"
              "7. Desligar termostato\n"
              "8. Armar sistema de segurança com gente em casa\n"
              "9. Armar sistema de segurança sem ninguém em casa\n"
              "10. Desarmar sistema de segurança\n"
              "11. Ver dispositivos ligados\n"
              "12. Contar dispositivos ligados\n"
              "0. Sair\n")
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            continuar = False
        elif opcao == '1':
            escolha = int(input("Tipo do dispositivo\n"
                                "1. Luz\n"
                                "2. Termostato\n"
                                "3. Sistema de Seguranca\n"))

            tipo = {1: 'luz', 2: 'termostato', 3: 'sistema_seguranca'}.get(escolha, None)
            if tipo is None:
                print("Tipo de dispositivo inválido.")
            else:
                nome = input("Nome do dispositivo: ").strip()
                ambiente = input("Nome do ambiente: ").strip()
                dispositivo = DispositivoFactory.criar_dispositivo(tipo, nome, ambiente)
                casa.adicionar_dispositivo(dispositivo)
        elif opcao == '2':
            status = obter_status_dispositivos(casa.ambientes)
            for s in status:
                print(s)
        elif opcao in ['3', '4', '5', '6', '7', '8', '9', '10']:
            nome = input("Nome do dispositivo: ").strip()
            dispositivo_encontrado = False
            for dispositivos in casa.ambientes.values():
                dispositivo = next((d for d in dispositivos if d.nome == nome), None)
                if dispositivo:
                    if opcao == '3' and isinstance(dispositivo, Luz):
                        dispositivo.ligar()
                    elif opcao == '4' and isinstance(dispositivo, Luz):
                        dispositivo.desligar()
                    elif opcao == '5' and isinstance(dispositivo, Termostato):
                        dispositivo.aquecer()
                    elif opcao == '6' and isinstance(dispositivo, Termostato):
                        dispositivo.esfriar()
                    elif opcao == '7' and isinstance(dispositivo, Termostato):
                        dispositivo.desligar()
                    elif opcao == '8' and isinstance(dispositivo, SistemaSeguranca):
                        dispositivo.armar_com_gente_em_casa()
                    elif opcao == '9' and isinstance(dispositivo, SistemaSeguranca):
                        dispositivo.armar_sem_gente_em_casa()
                    elif opcao == '10' and isinstance(dispositivo, SistemaSeguranca):
                        dispositivo.desarmar()
                    else:
                        print("Ação não suportada para este dispositivo.")
                    dispositivo_encontrado = True
            if not dispositivo_encontrado:
                print("Dispositivo não encontrado.")
        elif opcao == '11':
            print("Quantidade de dispositivos delisgados:\n")
            print(f"{dispositivos_desligados(casa.ambientes)}\n")
        elif opcao == '12':
            print("Dispositivos ligados:\n")
            print(f"{contar_dispositivos_ligados(casa.ambientes)}\n")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
