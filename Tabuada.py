print('Bem-vindo ao meu sistema de tabuada!')
operacao = input("Digite : para dividir ou x para multiplicar: ")

if operacao == ":":
    def tabuadadivis (numero):
        for i in range(1, 11):
            quociente = numero / i
            print(f"{numero} / {i} = {quociente}")

    try:
        numero = int(input("Tabuada de divisão do número: "))
        tabuadadivis(numero)
    except ValueError:
        print("ERRO: Digite apenas números!")


elif operacao == "x":
    def tabuadamulti (numero):
        for i in range(1, 11):
            quociente = numero * i
            print(f"{numero} x {i} = {quociente}")


    try:
        numero = int(input("Tabuada de multiplicação do número: "))
        tabuadamulti(numero)
    except ValueError:
        print("ERRO: Digite apenas números!")



else:
    ValueError
    print("ERRO: Digite ':' para dividir ou 'x' para multiplicar.")


