### Projeto: Sistema de Casa Inteligente

#### Objetivo
O objetivo deste projeto é projetar e implementar um sistema de casa inteligente abrangente que integra vários conceitos vistos durante a disciplina, como programação orientada a objetos, padrões de projeto, máquinas de estados usando a biblioteca `transitions`, e conceitos de programação funcional, como compreensões de listas e funções como `map`, `filter` e `reduce`, além de argumentos de linha de comando.

#### Visão Geral do Projeto
O projeto faz o gerenciamento de dispositivos inteligente, sendo eles: termostato, sistema de segurança e luzes. Cada um dos dispositivos, nessa implementação é limitado ao máximo 5 no total por default. Mas o usuário pode redefinir o limite total através de argumento no momento de executar o programa. A  partir da execução, o sistema é controlado pelo usuário através de menus em interface de linha de comando(CLI).

### Formas para executar o projeto

#### 1. Por argumento na linha de comando
Caso deseje utilizar o limite de devices definido por default:

##### 1.1 Deve-se digitar o comando **python main.py**

Caso deseje-se alterar o valor default para limite de dispositivos:

##### 1.2 Deve-se digitar o comando **python main.py --max_dispositivos**
Sendo o *, o número desejado de dispositivos.

#### 2. Pela IDE
Outra maneira é rodar o arquivo main através da opção 'Run' da própria IDE. Nesse caso não é possível alterar o limite de dispositivos, que será o default.

### Padrões de design utilizados
Os padrões utilizados foram:

**Singleton**: Foi utilizado de modo que a classe CasaInteligente tivesse uma única instância, controlando o acesso global à casa inteligente e mantendo o estado consistente.

**Observer**: Foi utilizado para notificar observadores sobre mudanças de estado nos dispositivos, permitindo reatividade e comunicação eficiente entre objetos.

**Factory**: Através da classe DispositivoFactory, foram criadas instâncias dos diferentes tipos de dispositivos de forma encapsulada, sem expor a lógica de criação.

### Como usar a CLI

#### 1. No menu principal deve ser escolhida uma opção de controle sobre os dispositivos. Desde criar, até ligar, desligar e etc. A opção desejada deve ser digitada por linha de comando. 
#### 2. No caso da opção adicionar dispositivos, no Menu principal opção 1, irá abrir um outro menu, que permitirá escolher entre os 3 tipos de dispositivos disponíveis.

O menu principal ficará em loop, até que a opção "Sair" seja escolhida. No caso, com a digitação de 0.