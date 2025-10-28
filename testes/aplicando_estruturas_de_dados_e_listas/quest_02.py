"""
Descrição
Uma empresa quer criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido.

Entrada
Lista de participantes e o tema escolhido por cada um.
Saída
Dicionário agrupando os participantes por tema.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
3
Lucas, Fotografia
Ana, Viagem
Carlos, Fotografia	Fotografia: Lucas, Carlos
Viagem: Ana
4
João, Música
Pedro, Música
Maria, Dança
Ana, Dança	Música: João, Pedro
Dança: Maria, Ana
5
Ana, Tecnologia
Carlos, Esportes
Maria, Tecnologia
Pedro, Música
João, Esportes	Tecnologia: Ana, Maria
Esportes: Carlos, João
Música: Pedro
"""
# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    posicao_espaco = linha.rfind(", ")
    
    participante = linha[:posicao_espaco].strip()
    tema = linha[posicao_espaco + 1:].strip()
    if tema not in eventos:
        eventos[tema] = [participante]
    else:
        eventos[tema].append(participante)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")