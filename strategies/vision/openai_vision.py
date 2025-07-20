import base64
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from config import OPENAI_API_KEY, OPENAI_LLM_MODEL
from strategies.prompts.base_prompt import get_base_prompt

def encode_image_to_base64(image_bytes: bytes) -> str:
    """Codifica bytes de uma imagem para uma string base64."""
    return base64.b64encode(image_bytes).decode("utf-8")

def analyze_image_with_prompt_langchain(image_bytes: bytes, question: str) -> str:
    """
    Usa LangChain para enviar a imagem e a pergunta para o modelo multimodal da OpenAI.
    """
    base64_image = encode_image_to_base64(image_bytes)
    system_prompt = get_base_prompt()

    llm = ChatOpenAI(
        model=OPENAI_LLM_MODEL, 
        api_key=OPENAI_API_KEY,
        temperature=0.4, # Um pouco mais de criatividade para a formatação do texto
        max_tokens=1000
    )

    human_message = HumanMessage(
        content=[
            {"type": "text", "text": system_prompt},
            {"type": "text", "text": f"Pergunta específica do usuário: {question}"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ]
    )

    response = llm.invoke([human_message])
    return response.content