# Código de exemplo em Py
# Tabuada com comprehension list

valor = int(input("Insira o valor para saber a tabuada: "))
tabuada = [f"{valor} x {i} = {valor * i}" for i in range(1, 11)]

for linha in tabuada:
    print(linha)
