lista=[]
escolha="sim"
while escolha=="sim":
    lista1=input("digite um item: ")
    lista.append(lista1)
    escolha=input("digite sim para continuar ou nao para parar: ")
escolha2=input("deseja adicionar um item a lista: ")
if escolha2=="sim":
    while escolha2=="sim":
        lista1=input("digite um item: ")
        lista.append(lista1)
        escolha2=input("digite sim para continuar ou nao para parar: ")
print(lista)
escolha3=input("deseja deletar um item da lista? ")
if escolha3=="sim":
    lista.remove(input("digite o nome do item que quer deletar: "))
    escolha3=input("digite sim para continuar ou nao para parar: ")
print(f"essa é sua lista de compras!{lista}")