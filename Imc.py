nome=input("Insira seu nome: ")
peso=int(input("Insira seu peso: "))
altura=float(input("Insira sua altura (em metros): "))
imc=0

def CALCULAAR_IMC(nome):
    imc= peso/(altura*altura)
    print(f"{nome}, o seu imc é {imc}")
imc=CALCULAAR_IMC(nome)