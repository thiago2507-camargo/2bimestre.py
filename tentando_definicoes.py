compras = ["pão", "café", "leite"]
print(compras)

#pode ser removida pelo nome ou pelo indice
compras.remove("café")

compras.remove("compras[2]")
print(compras)

#append acrescenta um item ao final da lista, só pode adicionar um por vez
compras.append("açucar")
print(compras)

#é preciso criar uma lista nova para receber os elementos ordenados da lista antiga
compras_ordenadas = sorted(compras)
print(compras_ordenadas)

for item in compras:
    print("-", item)
#o nome panela é um identificador dos itens dentro da lista, esses itens podem receber qualquer tipo de nome
for panela in compras:
    print("-", panela)    


