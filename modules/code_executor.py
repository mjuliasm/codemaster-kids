import sys
import io
import time
from contextlib import redirect_stdout, redirect_stderr
import traceback

class CodeExecutor:
    """Executor de código seguro com sandboxing básico"""
    
    # Funções e módulos permitidos
    ALLOWED_BUILTINS = {
        'print', 'len', 'range', 'int', 'float', 'str', 'list', 'dict', 'tuple',
        'set', 'bool', 'abs', 'round', 'sum', 'max', 'min', 'sorted', 'reversed',
        'enumerate', 'zip', 'map', 'filter', 'input', 'type', 'isinstance',
        'help', 'dir', 'id', 'hash', 'bin', 'hex', 'oct', 'ord', 'chr',
        'all', 'any', 'pow', 'divmod'
    }
    
    # Módulos permitidos
    ALLOWED_MODULES = ['math', 'random', 'datetime', 'json']
    
    # Variáveis de robótica simuladas
    ROBOTICS_NAMESPACE = {
        'LED_VERMELHO': 1,
        'LED_AMARELO': 2,
        'LED_VERDE': 3,
        'MOTOR_ESQUERDO': 4,
        'MOTOR_DIREITO': 5,
        'SENSOR_DISTANCIA': {'valor': 50},
        'SENSOR_LUZ': {'valor': 255},
        'ligar_led': lambda pin: f"LED {pin} ligado ✓",
        'desligar_led': lambda pin: f"LED {pin} desligado ✓",
        'motor_frente': lambda pin, velocidade: f"Motor {pin} em frente com {velocidade}% ✓",
        'motor_parar': lambda pin: f"Motor {pin} parado ✓",
        'ler_sensor': lambda sensor: f"Leitura do sensor: {sensor['valor']}",
    }
    
    @staticmethod
    def execute(code, timeout=10, include_robotics=False):
        """
        Executa código Python de forma segura
        
        Args:
            code: String com código Python
            timeout: Tempo máximo de execução em segundos
            include_robotics: Se deve incluir variáveis de robótica
        
        Returns:
            dict: {success, output, error, execution_time}
        """
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()
        
        # Preparar namespace seguro
        safe_namespace = {
            '__builtins__': {name: __builtins__[name] for name in CodeExecutor.ALLOWED_BUILTINS 
                           if name in __builtins__}
        }
        
        # Adicionar módulos permitidos
        for module_name in CodeExecutor.ALLOWED_MODULES:
            try:
                safe_namespace[module_name] = __import__(module_name)
            except ImportError:
                pass
        
        # Adicionar variáveis de robótica se solicitado
        if include_robotics:
            safe_namespace.update(CodeExecutor.ROBOTICS_NAMESPACE)
        
        start_time = time.time()
        
        try:
            with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                exec(code, safe_namespace)
            
            execution_time = time.time() - start_time
            
            if execution_time > timeout:
                return {
                    'success': False,
                    'output': output_buffer.getvalue(),
                    'error': f'Tempo limite excedido ({timeout}s)',
                    'execution_time': execution_time
                }
            
            return {
                'success': True,
                'output': output_buffer.getvalue(),
                'error': error_buffer.getvalue(),
                'execution_time': execution_time
            }
        
        except Exception as e:
            execution_time = time.time() - start_time
            error_message = f"{type(e).__name__}: {str(e)}\n\n"
            error_message += traceback.format_exc()
            
            return {
                'success': False,
                'output': output_buffer.getvalue(),
                'error': error_message,
                'execution_time': execution_time
            }
    
    @staticmethod
    def validate_code(code):
        """
        Valida código antes de executar
        
        Returns:
            tuple: (is_valid, error_message)
        """
        dangerous_keywords = ['__import__', 'eval', 'exec', 'compile', 'open', 
                             'input', 'file', '__', 'globals', 'locals', 'vars']
        
        code_lower = code.lower()
        
        for keyword in dangerous_keywords:
            if keyword in code_lower:
                # Permitir input com restrições
                if keyword == 'input':
                    continue
                return False, f"⚠️ Operação não permitida: {keyword}"
        
        return True, ""
    
    @staticmethod
    def format_output(output):
        """Formata a saída do código para exibição"""
        if not output:
            return "(Nenhuma saída)"
        return output.strip()
