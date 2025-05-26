#Maquina de lavar louça
import time
ligado=False
temperatura=0
tempo=0

def LIGAR(novo_tempo, nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado=True
        temperatura=nova_temperatura
        tempo=novo_tempo
        print(f"A maquina está ligada por {tempo} segundos na potência {temperatura}")
        INICIAR_CRONOMETRO(tempo)
    else:
        print("já ligada")

def DESLIGAR():
    global ligado
    if ligado:
        ligado=False

def INICIAR_CRONOMETRO(segundos):
    while segundos>0:
        print(f"Tempo restante: {segundos} segundos ", end="\r")
        time.sleep(1)
        segundos=segundos-1
    print("Tempo esgotado")

def STATUS():
    if ligado:
        print(f"Tempo: {tempo} segundos \n temperatura: {temperatura}")
    else:
        print("desligado")

def VIDRO():
    # temperatura=100
    # tempo=120
    LIGAR(120, 100)


def PLASTICO():
    # temperatura=21
    # tempo=60
    LIGAR(60, 21)

def METAL():
    # temperatura=30
    # tempo=120
    LIGAR(120, 30)

def PERSONALISADO(novo_tempo, nova_temperatura):
    
    LIGAR(novo_tempo, nova_temperatura)

escolha=int(input("Escolha o tipo de lavagem: 1-Vidro, 2-Plastico, 3-Metal, 4-Personalizado \n"))
if escolha==1:
    VIDRO()
elif escolha==2:
    PLASTICO()
elif escolha==3:
    METAL()
elif escolha==4:
    novo_tempo=int(input("Insira o tempo da lavagem: "))
    nova_temperatura=int(input("Insira a temperatura da lavagem: "))
    PERSONALISADO(novo_tempo, nova_temperatura)
    





