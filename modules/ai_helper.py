import os
from anthropic import Anthropic

class AIHelper:
    """Assistente de IA para ajudar na aprendizagem"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic()
        self.conversation_history = []
    
    def get_hint(self, lesson_content, student_name="Aluno"):
        """Gera uma dica para ajudar o aluno sem dar spoilers"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"""
                Você é um professor de programação para crianças de 11 anos.
                Uma criança chamada {student_name} está aprendendo este conteúdo:
                
                {lesson_content}
                
                Dê uma dica CURTA (máximo 2-3 linhas) para ajudá-lo a entender o conceito,
                SEM revelar a resposta. Use analogias com o mundo real.
                Fale em tom amigável e encorajador.
                """
            }]
        )
        
        return message.content[0].text
    
    def get_explanation(self, concept, level="básico", student_name="Aluno"):
        """Explica um conceito de forma simples e didática"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": f"""
                Você é um professor de programação para crianças de 11 anos.
                Explique o conceito de "{concept}" em nível {level}.
                
                Instruções:
                - Use exemplos do mundo real ou de robótica
                - Mantenha frases simples e claras
                - Inclua um exemplo prático de código
                - Fale para {student_name}
                - Seja entusiasmado e divertido
                
                Responda em português brasileiro.
                """
            }]
        )
        
        return message.content[0].text
    
    def debug_code(self, code, error_message):
        """Ajuda a debugar código que não funciona"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"""
                Um aluno de 11 anos está tendo um erro no seguinte código:
                
                ```python
                {code}
                ```
                
                Erro: {error_message}
                
                Por favor:
                1. Explique qual é o problema em linguagem simples
                2. Dê uma dica para corrigir SEM revelar a solução completa
                3. Se apropriado, mostre como seria a solução corrigida
                
                Seja amigável e encorajador!
                """
            }]
        )
        
        return message.content[0].text
    
    def suggest_next_steps(self, completed_lesson, current_level):
        """Sugere próximos passos na aprendizagem"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"""
                Um aluno de 11 anos completou a aula: "{completed_lesson}"
                Ele está no Nível {current_level}.
                
                Sugira 3 próximos passos interessantes para continuar aprendendo,
                em ordem de dificuldade crescente.
                Seja entusiasmado!
                """
            }]
        )
        
        return message.content[0].text
    
    def evaluate_code_quality(self, code, exercise_description):
        """Avalia a qualidade do código do aluno"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"""
                Um aluno de 11 anos escreveu este código para o exercício:
                "{exercise_description}"
                
                ```python
                {code}
                ```
                
                Por favor:
                1. Verifique se o código resolve o exercício corretamente
                2. Dê feedback positivo sobre o que foi feito bem
                3. Sugira 1-2 melhorias (sem ser crítico)
                4. Considere soluções mais elegantes se aplicável
                
                Seja encorajador, mesmo que o código tenha problemas!
                """
            }]
        )
        
        return message.content[0].text
    
    def chat(self, user_message, context=""):
        """Conversa com o aluno de forma educativa"""
        
        # Adicionar mensagem do usuário ao histórico
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Preparar system prompt
        system_prompt = f"""
        Você é Claude, um assistente de IA amigável que ajuda crianças de 11 anos a aprender programação.
        
        Suas características:
        - Fale em português brasileiro simples e divertido
        - Sempre encorajador e positivo
        - Relacione conceitos com robótica quando possível
        - Dê exemplos práticos
        - Nunca dê a resposta completa sem a criança tentar primeiro
        - Use emojis para deixar mais divertido
        - Seja curioso e faça perguntas para ajudar a criança a pensar
        
        Contexto da aula: {context}
        """
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            system=system_prompt,
            messages=self.conversation_history
        )
        
        assistant_response = message.content[0].text
        
        # Adicionar resposta do assistente ao histórico
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })
        
        # Limitar histórico a últimas 10 mensagens
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]
        
        return assistant_response
    
    def clear_history(self):
        """Limpa o histórico da conversa"""
        self.conversation_history = []
    
    def generate_challenge(self, topic, difficulty_level="fácil"):
        """Gera um desafio personalizado sobre um tópico"""
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": f"""
                Gere um desafio de programação em Python para uma criança de 11 anos.
                
                Tópico: {topic}
                Nível de dificuldade: {difficulty_level}
                
                O desafio deve:
                1. Ser claro e divertido
                2. Incluir a descrição do que fazer
                3. Se possível, relacionar com robótica
                4. Incluir um exemplo de entrada/saída esperada
                5. Ter pontos de bônus para solução criativa
                
                Formate a resposta assim:
                **Desafio**: [descrição]
                **Dificuldade**: {difficulty_level}
                **Entrada esperada**: [exemplo]
                **Saída esperada**: [exemplo]
                **Bônus**: [desafio extra]
                """
            }]
        )
        
        return message.content[0].text
