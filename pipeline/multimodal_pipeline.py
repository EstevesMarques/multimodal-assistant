from strategies.vision.openai_vision import analyze_image_with_prompt_langchain
from utils.logger import get_logger

logger = get_logger(__name__)

def process_image_and_question(image_bytes: bytes, question: str) -> str:
    """
    Recebe os BYTES da imagem e uma pergunta, envia para a estratégia 
    de visão e retorna a resposta em texto/markdown.
    """
    if not image_bytes or not question.strip():
        raise ValueError("Bytes da imagem e a pergunta não podem ser vazios.")

    try:
        logger.info("Iniciando análise com a estratégia de visão...")
        response = analyze_image_with_prompt_langchain(image_bytes, question)
        logger.info("Análise retornada com sucesso.")
        return response
    except Exception as e:
        logger.error(f"Erro na pipeline ao processar imagem e pergunta: {e}")
        raise e