from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_text_only(prompt: str) -> str:
    """
    Envia apenas texto para o modelo de linguagem da OpenAI (GPT-4o).
    Pode ser usado para perguntas sem imagem.
    """
    response = client.chat.completions.create(
        model=OPENAI_LLM_MODEL,
        messages=[
            {"role": "system", "content": "Você é um assistente especialista em nutrição."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=600,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()