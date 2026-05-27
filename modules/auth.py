import sqlite3
from datetime import datetime
import os

class UserAuth:
    def __init__(self, db_path="data/users.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                current_level INTEGER DEFAULT 1,
                total_points INTEGER DEFAULT 0,
                streak INTEGER DEFAULT 0,
                last_login TIMESTAMP
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                level INTEGER NOT NULL,
                lesson INTEGER NOT NULL,
                completed BOOLEAN DEFAULT 0,
                completed_at TIMESTAMP,
                points_earned INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                achievement_name TEXT NOT NULL,
                earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        conn.commit()
        conn.close()
    
    def register_user(self, username, name, age):
        """Registra um novo usuário"""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('''
                INSERT INTO users (username, name, age, created_at)
                VALUES (?, ?, ?, ?)
            ''', (username, name, age, datetime.now()))
            conn.commit()
            user_id = c.lastrowid
            conn.close()
            return user_id
        except sqlite3.IntegrityError:
            return None
    
    def get_user(self, username):
        """Recupera informações do usuário"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT id, name, age, current_level, total_points, streak FROM users WHERE username = ?', 
                  (username,))
        user = c.fetchone()
        conn.close()
        return user
    
    def update_login(self, username):
        """Atualiza último login e verifica streak"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE users SET last_login = ? WHERE username = ?', 
                  (datetime.now(), username))
        conn.commit()
        conn.close()
    
    def add_points(self, user_id, points):
        """Adiciona pontos ao usuário"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE users SET total_points = total_points + ? WHERE id = ?', 
                  (points, user_id))
        conn.commit()
        conn.close()
    
    def unlock_level(self, user_id, level):
        """Desbloqueia um nível"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE users SET current_level = ? WHERE id = ? AND current_level < ?', 
                  (level, user_id, level))
        conn.commit()
        conn.close()
    
    def add_achievement(self, user_id, achievement_name):
        """Adiciona uma conquista"""
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('''
                INSERT INTO achievements (user_id, achievement_name)
                VALUES (?, ?)
            ''', (user_id, achievement_name))
            conn.commit()
            conn.close()
            return True
        except:
            return False
    
    def get_achievements(self, user_id):
        """Retorna todas as conquistas do usuário"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT achievement_name FROM achievements WHERE user_id = ?', (user_id,))
        achievements = [row[0] for row in c.fetchall()]
        conn.close()
        return achievements
