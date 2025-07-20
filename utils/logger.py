import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """Configura e retorna um logger customizado."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Cria um handler para o console
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Cria um formatter e o adiciona ao handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Adiciona o handler ao logger
        logger.addHandler(handler)
        
    return logger