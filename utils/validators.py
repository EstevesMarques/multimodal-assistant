from PIL import Image

def validate_image(image: Image.Image) -> bool:
    """
    Verifica se a imagem fornecida é válida e tem dimensões mínimas aceitáveis.
    """
    if image is None:
        return False
    width, height = image.size
    return width > 50 and height > 50  # Exemplo: rejeita imagens muito pequenas ou vazias

def validate_prompt(prompt: str) -> bool:
    """
    Verifica se o prompt não está vazio e tem comprimento mínimo.
    """
    return bool(prompt and len(prompt.strip()) >= 5)
