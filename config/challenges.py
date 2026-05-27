"""
Desafios Extras e Projetos Integradores
"""

EXTRA_CHALLENGES = {
    1: [  # Nível 1
        {
            "id": 1,
            "title": "Calculadora Simples",
            "difficulty": "Fácil",
            "description": """
Crie uma calculadora que:
- Pede dois números
- Pergunta qual operação (+, -, *, /)
- Calcula e exibe o resultado

Dica: Use if/elif/else para cada operação
            """,
            "expected_output": "3 + 5 = 8",
            "bonus": "Trate divisão por zero com try/except"
        },
        {
            "id": 2,
            "title": "Jogo de Adivinhação",
            "difficulty": "Médio",
            "description": """
Crie um jogo onde:
- O programa escolhe um número de 1 a 100
- O usuário tenta adivinhar
- Diga se o número é maior ou menor
- Conte quantas tentativas

Dica: Use while True e break
            """,
            "expected_output": "Você acertou em 7 tentativas!",
            "bonus": "Limite a 10 tentativas máximo"
        }
    ],
    2: [  # Nível 2
        {
            "id": 1,
            "title": "Agenda de Contatos",
            "difficulty": "Médio",
            "description": """
Crie uma agenda onde:
- Adicione contatos (nome, telefone, email)
- Liste todos os contatos
- Busque um contato pelo nome
- Delete um contato

Use dicionários para cada contato e listas para armazenar
            """,
            "expected_output": "João - 11999999999 - joao@email.com",
            "bonus": "Salve em arquivo (JSON)"
        },
        {
            "id": 2,
            "title": "Processador de Texto",
            "difficulty": "Médio",
            "description": """
Processe um texto para:
- Contar palavras e caracteres
- Encontrar a palavra mais frequente
- Converter para maiúsculas/minúsculas
- Remover espaços em branco

Use strings, listas e dicionários
            """,
            "expected_output": "Texto tem 150 palavras, 800 caracteres",
            "bonus": "Analise sentimento (positivo/negativo)"
        }
    ],
    3: [  # Nível 3
        {
            "id": 1,
            "title": "Algoritmo de Ordenação",
            "difficulty": "Médio",
            "description": """
Implemente diferentes algoritmos de ordenação:
- Bubble Sort
- Selection Sort
- Insertion Sort

Compare o desempenho com listas de diferentes tamanhos
            """,
            "expected_output": "[1, 2, 3, 4, 5] - Bubble Sort: 0.001s",
            "bonus": "Implemente Quick Sort (mais rápido)"
        },
        {
            "id": 2,
            "title": "Labirinto com Recursão",
            "difficulty": "Difícil",
            "description": """
Use recursão para encontrar caminho em um labirinto:
- Represente como matriz (0 = caminho, 1 = parede)
- Use backtracking para encontrar saída
- Marque o caminho encontrado

Este é um projeto que um robô poderia usar!
            """,
            "expected_output": "Caminho encontrado: (0,0) -> (0,1) -> (1,1)...",
            "bonus": "Encontre o caminho mais curto (BFS)"
        }
    ],
    4: [  # Nível 4 - SQL
        {
            "id": 1,
            "title": "Banco de Dados de Robôs",
            "difficulty": "Médio",
            "description": """
Crie um banco de dados com:
- Tabela de robôs (id, nome, velocidade_max, bateria%)
- Tabela de missões (id, robo_id, data, resultado)
- Tabela de sensores (id, robo_id, tipo, última_leitura)

Execute queries para:
- Listar robôs com bateria baixa
- Contar missões por robô
- Encontrar sensor com leitura anormal
            """,
            "expected_output": "Robô 3 com bateria 15%",
            "bonus": "Use JOINs para cruzar dados de múltiplas tabelas"
        }
    ],
    5: [  # Nível 5 - IA
        {
            "id": 1,
            "title": "Preditor Simples",
            "difficulty": "Médio",
            "description": """
Crie um modelo simples que:
- Coleta dados de temperatura vs. velocidade_fan
- Treina em dados históricos
- Prevê velocidade do ventilador para nova temperatura

Use machine learning simples (regressão)
            """,
            "expected_output": "Temperatura 35°C -> Ventilador 70%",
            "bonus": "Calcule a acurácia do modelo"
        }
    ]
}

PROJECT_IDEAS = {
    "integradores_nivel_1": [
        {
            "name": "Simulador de LED RGB",
            "description": "Controle um LED RGB colorido com Python",
            "skills": ["variáveis", "funções", "loops"],
            "robotics": "LED RGB real com Arduino"
        },
        {
            "name": "Contador de Passos",
            "description": "Simule um contador de passos como relógio inteligente",
            "skills": ["variáveis", "operações", "if/else"],
            "robotics": "Sensor acelerômetro MPU6050"
        }
    ],
    "integradores_nivel_2": [
        {
            "name": "Sistema de Leitura de Sensores",
            "description": "Leia múltiplos sensores e armazene dados",
            "skills": ["listas", "dicionários", "loops"],
            "robotics": "Múltiplos sensores: distância, luz, temperatura"
        },
        {
            "name": "Manipulador de Dados de Voo",
            "description": "Processe dados de drone",
            "skills": ["strings", "listas", "tratamento de erros"],
            "robotics": "Telemetria de drone"
        }
    ],
    "integradores_nivel_3": [
        {
            "name": "Navegação de Robô",
            "description": "Use algoritmos para encontrar caminho ótimo",
            "skills": ["algoritmos", "recursão", "complexidade"],
            "robotics": "Robô autônomo encontra melhor rota"
        }
    ],
    "integradores_nivel_4": [
        {
            "name": "Histórico de Robô",
            "description": "Banco de dados de todas as operações do robô",
            "skills": ["SQL", "JOINs", "queries complexas"],
            "robotics": "Rastrear histórico completo de sensores"
        }
    ],
    "integradores_nivel_5": [
        {
            "name": "Robô Inteligente",
            "description": "Robô que aprende e melhora com o tempo",
            "skills": ["IA", "machine learning", "previsão"],
            "robotics": "Robô autônomo com AI"
        }
    ]
}

def get_challenges_for_level(level):
    """Retorna desafios para um nível"""
    return EXTRA_CHALLENGES.get(level, [])

def get_projects_for_level(level):
    """Retorna projetos para um nível"""
    key = f"integradores_nivel_{level}"
    return PROJECT_IDEAS.get(key, [])

def get_all_challenges():
    """Retorna todos os desafios"""
    return EXTRA_CHALLENGES

def get_all_projects():
    """Retorna todos os projetos"""
    return PROJECT_IDEAS
