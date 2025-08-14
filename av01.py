destinos = [  
    {'nome':'Maceió', 'clima': 'quente', 'tipo': 'natureza', 'preco':1500},
    {'nome':'Recife', 'clima': 'quente', 'tipo': 'urbano', 'preco':1100},
    {'nome':'Garanhus', 'clima': 'frio', 'tipo': 'natureza', 'preco':800},
    {'nome':'São Paulo', 'clima': 'frio', 'tipo': 'urbano', 'preco':2500},
]

def recomendar_destino(clima, tipo, preco_max):
    for destino in destinos:
        if destino['clima'] == clima and destino['tipo'] == tipo and destino['preco'] <= preco_max:
            return (f"Recomendamos:{destino['nome']} - Combina com seu tipo "
                    f"{destino['tipo']} - e o seu orçamento {destino['preco']}")
    return "Nenhum destino encontrado"  # Mova o return para depois do loop

# Coleta de dados:
clima = input("Digite o clima: ").strip().lower()
tipo = input("Digite o tipo: ").strip().lower()
orcamento = float(input("Qual o seu orçamento disponivel? "))

# resposta
print(recomendar_destino(clima, tipo, orcamento))