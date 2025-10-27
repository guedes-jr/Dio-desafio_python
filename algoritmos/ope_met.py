"""
Vamos solicitar como entrada dois números e depois vamos 
realizar uma operação simples entre eles.
"""
# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Mostra opções de operação
print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação: ")

# Executa a operação escolhida
if opcao == "1":
    resultado = num1 + num2
    operacao = "soma"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "subtração"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "multiplicação"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        resultado = "Erro! Divisão por zero."
        operacao = "divisão"
else:
    resultado = False
    operacao = "nenhuma"

if not resultado:
    print("Operação inválida!")
else:
    print(f"\nO resultado da {operacao} é: {resultado}")
