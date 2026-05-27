class Gamification:
    """Sistema de gamificação para motivar alunos"""
    
    LEVELS_INFO = {
        1: {
            "name": "🟢 Nível 1: Fundamentos Python",
            "description": "Aprenda os conceitos básicos de programação",
            "lessons": 5,
            "points_required": 0,
            "color": "#00FF00"
        },
        2: {
            "name": "🟡 Nível 2: Python Intermediário",
            "description": "Estruturas de dados e manipulação de dados",
            "lessons": 5,
            "points_required": 500,
            "color": "#FFFF00"
        },
        3: {
            "name": "🟠 Nível 3: Algoritmos & Estruturas de Dados",
            "description": "Aprofunde em algoritmos e complexidade",
            "lessons": 5,
            "points_required": 1200,
            "color": "#FFA500"
        },
        4: {
            "name": "🔴 Nível 4: Banco de Dados com SQL",
            "description": "Domine consultas e design de banco de dados",
            "lessons": 5,
            "points_required": 2000,
            "color": "#FF0000"
        },
        5: {
            "name": "🟣 Nível 5: IA e Machine Learning",
            "description": "Explore inteligência artificial e previsões",
            "lessons": 5,
            "points_required": 3000,
            "color": "#9900FF"
        }
    }
    
    ACHIEVEMENTS = {
        "first_code": {
            "name": "👶 Seu Primeiro Código",
            "description": "Execute seu primeiro programa com sucesso",
            "points": 50
        },
        "level_1_complete": {
            "name": "🎓 Graduado Nível 1",
            "description": "Complete todas as aulas do Nível 1",
            "points": 200
        },
        "python_master": {
            "name": "🐍 Mestre em Python",
            "description": "Complete 10 desafios de Python",
            "points": 300
        },
        "sql_wizard": {
            "name": "🧙 Assistente SQL",
            "description": "Complete 10 desafios de SQL",
            "points": 300
        },
        "robot_engineer": {
            "name": "🤖 Engenheiro de Robótica",
            "description": "Complete um projeto de integração com robótica",
            "points": 250
        },
        "ai_explorer": {
            "name": "🤖 Explorador de IA",
            "description": "Complete o Nível 5 com sucesso",
            "points": 500
        },
        "100_day_streak": {
            "name": "🔥 100 Dias em Fogo",
            "description": "Mantenha uma sequência de 100 dias",
            "points": 1000
        },
        "code_warrior": {
            "name": "⚔️ Guerreiro do Código",
            "description": "Complete 50 desafios",
            "points": 500
        },
        "perfect_score": {
            "name": "💯 Pontuação Perfeita",
            "description": "Obtenha 100 pontos em um desafio",
            "points": 150
        }
    }
    
    @staticmethod
    def get_level_info(level):
        """Retorna informações sobre um nível"""
        return Gamification.LEVELS_INFO.get(level, {})
    
    @staticmethod
    def get_achievement_info(achievement_id):
        """Retorna informações sobre uma conquista"""
        return Gamification.ACHIEVEMENTS.get(achievement_id, {})
    
    @staticmethod
    def calculate_level_from_points(points):
        """Calcula o nível baseado em pontos"""
        for level in range(5, 0, -1):
            if points >= Gamification.LEVELS_INFO[level]["points_required"]:
                return level
        return 1
    
    @staticmethod
    def calculate_progress(current_points, next_level):
        """Calcula progresso até o próximo nível"""
        current_requirement = Gamification.LEVELS_INFO[next_level]["points_required"]
        if next_level == 1:
            prev_requirement = 0
        else:
            prev_requirement = Gamification.LEVELS_INFO[next_level - 1]["points_required"]
        
        progress_needed = current_requirement - prev_requirement
        progress_made = current_points - prev_requirement
        
        if progress_needed == 0:
            return 100
        
        percentage = (progress_made / progress_needed) * 100
        return min(100, max(0, percentage))
    
    @staticmethod
    def get_all_levels():
        """Retorna todos os níveis"""
        return Gamification.LEVELS_INFO
    
    @staticmethod
    def get_all_achievements():
        """Retorna todas as conquistas"""
        return Gamification.ACHIEVEMENTS
