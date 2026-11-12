while True:
    n1 = int(input("Digite o primeiro número: "))
    operador = input("Digite um operador (+, -, * ou /): ")
    n2 = int(input("Digite o segundo número: "))

    numeros_validos = None
    n1_float = 0 
    n2_float = 0
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Números invalidos, digite novamente!")
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Operador não permitido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    resposta = 0

    if operador == "+":
        resposta = n1 + n2
    elif operador == "-":
        resposta = n1 - n2
    elif operador == "*":
        resposta = n1 * n2;
    elif operador == "/":
        resposta = n1 / n2

    print("\n",f"Resposta: {resposta}", "\n")
    sair = input("Quer sair? [S]im | [N]ão ").lower().startswith("s")
    if sair:
        break
