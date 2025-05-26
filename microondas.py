import time 

#variaveis globais
ligado=False
tempo=0
potencia=0

def LIGAR(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado=True
        tempo= novo_tempo
        potencia= nova_potencia
        print(f"Microondas ligado por {tempo} segundos na potência {potencia}")
        INICIAR_CRONOMETRO(tempo)
        DESLIGAR()  #desligar automaticamente
    else:
        print("O microondas já está ligado")

def DESLIGAR():
    global ligado
    if ligado:
        ligado=False
        print("O microondas está desligado")
    else:
        print("O microondas já está desligado")

def STATUS():
    if ligado:
        print(f"Tempo: {tempo} segundos /n potência: {potencia}")
    else:
        print("desligado")


def INICIAR_CRONOMETRO(segundos):
    while segundos>0:
        print(f"Tempo restante: {segundos} segundos ", end="\r")
        time.sleep(1)
        segundos=segundos-1

    print("Tempo esgotado")


def PIPOCA():
    LIGAR(30,100)

def DESCONGELAR():
    LIGAR(60, 60)

tempo=int(input("Tempo: "))
potencia=int(input("Potência: "))
LIGAR(tempo, potencia)

