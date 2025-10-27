"""
Agora vamos solicitar uma string e um número inteiro com entrada. 
Depois teremos que retornar a string repetida o número de vezes 
que foi informado.
"""
# Solicita os dados ao usuário
texto = " " + input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
resultado = texto * numero

# Exibe o resultado
print("Resultado:", resultado.strip())
