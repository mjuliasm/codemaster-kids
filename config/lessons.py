LESSONS = {
    1: {  # Nível 1: Fundamentos Python
        "name": "Fundamentos Python",
        "lessons": [
            {
                "id": 1,
                "title": "Variáveis e Tipos de Dados",
                "description": "Aprenda como armazenar informações em programação",
                "content": """
# Variáveis e Tipos de Dados 🏠

## O que é uma variável?
Uma variável é como uma caixa que guarda informações. Você dá um nome para a caixa e coloca dados dentro.

## Exemplo Básico:
```python
nome = "João"
idade = 11
altura = 1.50
é_estudante = True

print(nome)
print(idade)
print(altura)
```

## Tipos de Dados:
- **String (texto)**: "João", "Python"
- **Integer (inteiro)**: 11, -5, 100
- **Float (decimal)**: 1.50, 3.14
- **Boolean (verdadeiro/falso)**: True, False

## Nomes de Variáveis:
- Podem conter letras, números e underscore
- Não podem começar com número
- Em Python, usamos nome_da_variavel (com underscore)

## Desafio 🤖
Crie variáveis para guardar: seu nome, sua idade, sua altura e se você é estudante.
Imprima todas as informações!
                """,
                "challenge": "Crie 4 variáveis com seu nome, idade, altura e status de estudante. Imprima-as.",
                "robotics": "Assim como você armazena dados em variáveis, um robô armazena dados dos sensores (temperatura, distância, etc.)"
            },
            {
                "id": 2,
                "title": "Operações Matemáticas",
                "description": "Realize cálculos com Python",
                "content": """
# Operações Matemáticas 🔢

## Operadores Básicos:
- Adição: +
- Subtração: -
- Multiplicação: *
- Divisão: /
- Divisão inteira: //
- Resto (módulo): %
- Potência: **

## Exemplo:
```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

## Ordem de Operações:
A ordem é importante! Potência → Multiplicação/Divisão → Adição/Subtração

## Desafio 🤖
Calcule o preço final de um produto com imposto!
                """,
                "challenge": "Guarde o preço de um produto (100) e o imposto (15%). Calcule o preço final.",
                "robotics": "Um robô usa matemática para calcular a velocidade do motor, a distância percorrida, etc."
            },
            {
                "id": 3,
                "title": "Estrutura if/else",
                "description": "Faça decisões no código",
                "content": """
# Estrutura if/else 🚦

## O que é if/else?
É uma forma de o código tomar decisões baseado em condições.

## Exemplo Básico:
```python
idade = 11
if idade >= 11:
    print("Você pode aprender programação!")
else:
    print("Ainda é muito jovem")
```

## Operadores de Comparação:
- == (igual)
- != (diferente)
- > (maior)
- < (menor)
- >= (maior ou igual)
- <= (menor ou igual)

## Exemplo com múltiplas condições:
```python
nota = 85
if nota >= 90:
    print("Excelente!")
elif nota >= 80:
    print("Muito bom!")
elif nota >= 70:
    print("Bom!")
else:
    print("Precisa estudar mais")
```

## Desafio 🤖
Faça um programa que verifique a velocidade de um robô e diga se está rápido demais!
                """,
                "challenge": "Crie um programa que veja a idade do usuário e diga se pode aprender programação (11+)",
                "robotics": "Um robô precisa tomar decisões! Se a distância do obstáculo < 10cm, PARAR!"
            },
            {
                "id": 4,
                "title": "Loops - for",
                "description": "Repita ações várias vezes",
                "content": """
# Loops - for 🔄

## O que é um loop?
É uma forma de repetir código várias vezes sem escrevê-lo de novo.

## Loop for básico:
```python
for i in range(5):
    print(i)    # Imprime 0, 1, 2, 3, 4
```

## Entendendo range():
- range(5) → 0, 1, 2, 3, 4
- range(1, 6) → 1, 2, 3, 4, 5
- range(0, 10, 2) → 0, 2, 4, 6, 8 (de 2 em 2)

## Exemplo - Tabuada:
```python
numero = 7
for i in range(1, 11):
    print(f"{numero} × {i} = {numero * i}")
```

## Loop sobre lista:
```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

## Desafio 🤖
Crie um loop que imprima a tabuada de qualquer número!
                """,
                "challenge": "Imprima a tabuada do número 6 (de 1 até 10)",
                "robotics": "Um robô precisa repetir ações! Acender 5 LEDs: for LED in [1,2,3,4,5]"
            },
            {
                "id": 5,
                "title": "Funções Básicas",
                "description": "Crie seu próprio código reutilizável",
                "content": """
# Funções Básicas 📦

## O que é uma função?
Uma função é um bloco de código que realiza uma tarefa específica.
Você cria uma vez e usa várias vezes!

## Estrutura básica:
```python
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("João")
saudar("Maria")
```

## Função com retorno:
```python
def somar(a, b):
    resultado = a + b
    return resultado

total = somar(5, 3)
print(total)  # 8
```

## Função com múltiplos parâmetros:
```python
def apresentar(nome, idade, cidade):
    print(f"Meu nome é {nome}, tenho {idade} anos e moro em {cidade}")

apresentar("João", 11, "São Paulo")
```

## Boas práticas:
- Nomes descritivos: calcular_media(), saudar_usuario()
- Documentação: docstring explicando o que faz

## Desafio 🤖
Crie uma função que controle um motor de robô!
                """,
                "challenge": "Crie uma função que calcule a área de um retângulo (largura × altura)",
                "robotics": "Funções são ótimas para controlar robôs: ligar_motor(velocidade), ler_sensor(tipo)"
            }
        ]
    },
    2: {  # Nível 2: Python Intermediário
        "name": "Python Intermediário",
        "lessons": [
            {
                "id": 1,
                "title": "Listas",
                "description": "Trabalhe com coleções de dados",
                "content": """
# Listas 📝

## O que é uma lista?
Uma lista é uma coleção de items em uma determinada ordem.

## Criando listas:
```python
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
misturada = [1, "texto", 3.14, True]
```

## Acessando elementos:
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])    # maçã
print(frutas[1])    # banana
print(frutas[-1])   # laranja (último)
```

## Métodos úteis:
```python
frutas = ["maçã", "banana"]
frutas.append("laranja")      # Adiciona ao final
frutas.insert(0, "uva")       # Insere na posição 0
frutas.remove("banana")       # Remove um item
comprimento = len(frutas)     # Número de items
```

## Desafio 🤖
Crie uma lista de leituras de sensor e encontre o valor máximo!
                """,
                "challenge": "Crie uma lista com 5 números e imprima: primeiro, último e comprimento",
                "robotics": "Um robô coleta dados dos sensores em uma lista para análise!"
            },
            {
                "id": 2,
                "title": "Dicionários",
                "description": "Organize dados por chave-valor",
                "content": """
# Dicionários 🔑

## O que é um dicionário?
Um dicionário guarda pares de chave-valor, como um dicionário real!

## Criando dicionários:
```python
aluno = {
    "nome": "João",
    "idade": 11,
    "escola": "Escola ABC"
}

print(aluno["nome"])   # João
print(aluno["idade"])  # 11
```

## Adicionando itens:
```python
aluno["matricula"] = 12345
aluno["nota"] = 9.5
```

## Métodos úteis:
```python
aluno.get("nome")           # Pega o valor
aluno.keys()                # Pega todas as chaves
aluno.values()              # Pega todos os valores
aluno.items()               # Pega pares chave-valor
```

## Desafio 🤖
Crie um dicionário com informações de um robô!
                """,
                "challenge": "Crie um dicionário com dados de um robô (nome, velocidade, bateria%)",
                "robotics": "Cada robô tem múltiplas propriedades: velocidade, bateria, sensores!"
            },
            {
                "id": 3,
                "title": "Loops com while",
                "description": "Repita até uma condição ser falsa",
                "content": """
# Loops com while 🔄

## O que é um while?
Um loop que continua enquanto uma condição é verdadeira.

## Exemplo básico:
```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
```

## Diferença for vs while:
- **for**: você sabe quantas vezes vai repetir
- **while**: continua até uma condição ser falsa

## Exemplo prático:
```python
numero = 1
while numero <= 10:
    print(numero * 2)
    numero = numero + 1
```

## ⚠️ Evite loops infinitos!
```python
while True:
    print("Será impresso para sempre!")
    # Precisa de um break!
```

## Usando break:
```python
numero = 0
while True:
    if numero > 5:
        break
    print(numero)
    numero = numero + 1
```

## Desafio 🤖
Simule um robô que se move enquanto não encontrar um obstáculo!
                """,
                "challenge": "Crie um while que imprima números de 1 até o usuário digitar 'parar'",
                "robotics": "Robôs frequentemente usam: while robo_esta_em_movimento: continuar_movimento()"
            },
            {
                "id": 4,
                "title": "Manipulação de Strings",
                "description": "Trabalhe com textos de forma avançada",
                "content": """
# Manipulação de Strings 📝

## Strings úteis:
```python
texto = "Python é Incrível"

# Transformações
print(texto.lower())           # python é incrível
print(texto.upper())           # PYTHON É INCRÍVEL
print(texto.replace("Python", "Programação"))

# Verificações
print(texto.startswith("Python"))      # True
print(texto.endswith("!"))             # False
print("Incrível" in texto)             # True

# Divisão e junção
palavras = texto.split()       # ["Python", "é", "Incrível"]
novo = "-".join(palavras)      # Python-é-Incrível

# Comprimento
print(len(texto))              # 18
```

## f-strings (formatação):
```python
nome = "João"
idade = 11
print(f"Olá, meu nome é {nome} e tenho {idade} anos")
```

## Desafio 🤖
Processe mensagens recebidas por um robô!
                """,
                "challenge": "Pegue um texto e imprima invertido (ao contrário)",
                "robotics": "Um robô precisa processar comandos em string: 'FRENTE', 'ESQUERDA', 'PARAR'"
            },
            {
                "id": 5,
                "title": "Tratamento de Erros",
                "description": "Lide com erros graciosamente",
                "content": """
# Tratamento de Erros 🛡️

## O que é um erro?
Um erro acontece quando algo dá errado no programa.
Em vez de o programa quebrar, podemos tratar o erro!

## Estrutura try/except:
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
except ValueError:
    print("Por favor, digite um número válido!")
```

## Tratando qualquer erro:
```python
try:
    # código que pode ter erro
except:
    print("Algo deu errado!")
```

## Else e finally:
```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Inválido!")
else:
    print(f"Você digitou: {numero}")
finally:
    print("Fim do programa")  # Sempre executa
```

## Desafio 🤖
Faça um programa que trata erros de entrada do usuário!
                """,
                "challenge": "Peça um número e trate o erro se não for número",
                "robotics": "Um robô precisa lidar com erros de sensores: leitura_falha? Tentar novamente!"
            }
        ]
    },
    3: {  # Nível 3: Algoritmos
        "name": "Algoritmos e Estruturas de Dados",
        "lessons": [
            {
                "id": 1,
                "title": "Busca e Ordenação",
                "description": "Encontre e organize dados eficientemente",
                "content": """
# Busca e Ordenação 🔍

## Busca Linear:
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

print(busca_linear(numeros, 5))  # 4
```

## Ordenação com sort():
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Ordem reversa
numeros.sort(reverse=True)
```

## Bubble Sort (entender o algoritmo):
```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

## Desafio 🤖
Ordene leituras de sensores de um robô!
                """,
                "challenge": "Ordene uma lista de números e encontre o valor maior",
                "robotics": "Um robô coleta múltiplas leituras de sensores e precisa encontrar a máxima!"
            },
            {
                "id": 2,
                "title": "Recursão",
                "description": "Uma função que chama a si mesma",
                "content": """
# Recursão 🔄

## O que é recursão?
Uma função que chama a si mesma para resolver problemas menores.

## Partes da recursão:
1. **Caso base**: quando parar
2. **Caso recursivo**: chamar a função novamente

## Exemplo - Fatorial:
```python
def fatorial(n):
    # Caso base
    if n == 1 or n == 0:
        return 1
    # Caso recursivo
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # 5 × 4 × 3 × 2 × 1 = 120
```

## Exemplo - Contagem regressiva:
```python
def contagem_regressiva(n):
    if n == 0:
        print("Pronto!")
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(5)
```

## ⚠️ Cuidado com recursão infinita!

## Desafio 🤖
Use recursão para calcular o comprimento de uma lista!
                """,
                "challenge": "Use recursão para calcular a soma de todos os números de 1 até N",
                "robotics": "Um robô explora um labirinto recursivamente: explorar_caminho()"
            }
        ]
    },
    4: {  # Nível 4: SQL
        "name": "Banco de Dados com SQL",
        "lessons": [
            {
                "id": 1,
                "title": "Introdução ao SQL",
                "description": "Aprenda a linguagem dos bancos de dados",
                "content": """
# SQL - Structured Query Language 🗂️

## O que é SQL?
SQL é uma linguagem para comunicar com bancos de dados.

## Criando uma tabela:
```sql
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    nota REAL
);
```

## Inserindo dados:
```sql
INSERT INTO alunos (id, nome, idade, nota)
VALUES (1, 'João', 11, 9.5);

INSERT INTO alunos (id, nome, idade, nota)
VALUES (2, 'Maria', 11, 8.5);
```

## SELECT básico:
```sql
SELECT * FROM alunos;
SELECT nome, nota FROM alunos;
SELECT * FROM alunos WHERE idade = 11;
```

## Desafio 🤖
Crie uma tabela para sensores de robô!
                """,
                "challenge": "Crie uma tabela de robôs com id, nome, velocidade_max, bateria%",
                "robotics": "Bancos de dados armazenam histórico de operações dos robôs!"
            },
            {
                "id": 2,
                "title": "SELECT Avançado",
                "description": "Realize buscas sofisticadas",
                "content": """
# SELECT Avançado 🔍

## ORDER BY - Ordenação:
```sql
SELECT * FROM alunos ORDER BY nota DESC;
SELECT * FROM alunos ORDER BY nome ASC;
```

## WHERE com múltiplas condições:
```sql
SELECT * FROM alunos WHERE idade = 11 AND nota > 8;
SELECT * FROM alunos WHERE idade = 11 OR nota > 9;
```

## LIKE - Busca de texto:
```sql
SELECT * FROM alunos WHERE nome LIKE 'J%';
SELECT * FROM alunos WHERE nome LIKE '%a';
```

## LIMIT - Limitar resultados:
```sql
SELECT * FROM alunos LIMIT 5;
SELECT * FROM alunos ORDER BY nota DESC LIMIT 3;
```

## COUNT - Contar resultados:
```sql
SELECT COUNT(*) FROM alunos;
SELECT COUNT(*) FROM alunos WHERE nota > 8;
```

## Desafio 🤖
Encontre os robôs com bateria baixa!
                """,
                "challenge": "Selecione alunos com nota maior que 8, ordenados por nota DESC",
                "robotics": "Encontre robôs com sensores com leitura anormal!"
            }
        ]
    },
    5: {  # Nível 5: IA
        "name": "IA e Machine Learning",
        "lessons": [
            {
                "id": 1,
                "title": "Introdução à IA",
                "description": "Entenda como máquinas podem aprender",
                "content": """
# Introdução à IA 🤖

## O que é IA?
IA significa que o computador pode aprender e tomar decisões,
similar a como você aprende!

## Exemplos de IA:
- Seu celular reconhecendo sua voz
- YouTube sugerindo vídeos
- ChatGPT respondendo perguntas
- Robôs autônomos aprendendo a navegar

## Machine Learning:
É quando o computador **aprende** com dados,
em vez de seguir instruções prontas.

## Como funciona:
1. **Dados**: Coletar informações (temperatura, distância, etc)
2. **Treino**: Ensinar ao algoritmo reconhecer padrões
3. **Previsão**: Usar o modelo para prever novos dados

## Exemplo simples:
```python
# Seu robô coleta dados de temperatura
temperaturas = [20, 21, 19, 22, 20, 21]
# Pode prever que a próxima será ~20-21°C
```

## Desafio 🤖
Pense em um padrão que seu robô poderia aprender!
                """,
                "challenge": "Liste 3 exemplos de IA que você usa no dia a dia",
                "robotics": "Um robô inteligente aprende com erros e se melhora!"
            }
        ]
    }
}
