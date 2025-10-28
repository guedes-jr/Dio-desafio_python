"""
Descrição
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

Entrada
Uma lista contendo os números dos quartos disponíveis.
Uma lista contendo os números dos quartos solicitados pelos clientes.
Saída
Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
101 102 103 104
102 105 101 103	Reservas confirmadas: 102 101 103
Reservas recusadas: 105
201 202 203 204 205
205 202 208 201 203	Reservas confirmadas: 205 202 201 203
Reservas recusadas: 208
10 20 30 40 50
25 30 10 40 50 60	Reservas confirmadas: 30 10 40 50
Reservas recusadas: 25 60
"""
def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = []

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva)
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()