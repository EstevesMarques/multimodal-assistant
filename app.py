import streamlit as st

from pipeline.multimodal_pipeline import process_image_and_question
from utils.logger import get_logger

# --- Configurações da Página ---
st.set_page_config(
    page_title="🥗 Assistente Nutricional IA",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",
)
logger = get_logger("main_app")

# --- CSS Personalizado ---
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border: 1px solid #e6e6e6; border-radius: 15px; padding: 25px;
        background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease-in-out;
    }
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"]:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .stButton>button {
        border-radius: 10px; border: 2px solid #2E8B57; color: #2E8B57;
        background-color: transparent; font-weight: bold; transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        border-color: #2E8B57; background-color: #2E8B57; color: white;
    }
    .stButton>button:focus:not(:active) { border-color: #2E8B57; color: #2E8B57; }
    h1, p { text-align: center; }
    h1 { color: #2E8B57; }
    [data-testid="stImage"] img { border-radius: 10px; max-height: 400px; object-fit: cover; }
    [data-testid="stTextInput"] { border: 1px solid #e6e6e6; border-radius: 10px; padding: 8px 12px; transition: border-color 0.3s, box-shadow 0.3s; }
    [data-testid="stTextInput"]:focus-within { border-color: #2E8B57; box-shadow: 0 0 0 2px rgba(46, 139, 87, 0.2); }
</style>
""", unsafe_allow_html=True)


# --- Título e Subtítulo ---
st.title("🥗 Assistente Nutricional com IA")
st.markdown("<p>Uma forma inteligente de entender sua alimentação. Envie uma foto e tire suas dúvidas.</p>", unsafe_allow_html=True)
st.markdown("---")

DEFAULT_QUESTION = "Quantas calorias tem este prato? Faça uma análise completa."

def set_default_question_if_empty():
    """Se o campo de pergunta estiver vazio, preenche com o valor padrão."""
    if not st.session_state.question_input:
        st.session_state.question_input = DEFAULT_QUESTION

# --- Layout Principal ---
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container():
        st.header("📸 1. Envie sua Refeição")
        source = st.radio("Fonte da imagem:", ("Tirar uma foto", "Enviar um arquivo"), horizontal=True, label_visibility="collapsed")

        image_bytes = None
        if source == "Tirar uma foto":
            camera_photo = st.camera_input("Aponte a câmera para o prato", label_visibility="collapsed")
            if camera_photo: image_bytes = camera_photo.getvalue()
        else:
            uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
            if uploaded_file: image_bytes = uploaded_file.getvalue()

        if image_bytes: st.session_state['image_bytes'] = image_bytes
        if 'image_bytes' in st.session_state:
            st.image(st.session_state['image_bytes'], caption="Imagem pronta para análise.", use_column_width=True)

        st.header("💬 2. Faça sua Pergunta")
        question = st.text_input("Pergunta", placeholder=DEFAULT_QUESTION, key="question_input", label_visibility="collapsed")
        
        analyze_button = st.button(
            "Analisar Refeição", 
            use_container_width=True, 
            on_click=set_default_question_if_empty
        )

with col2:
    with st.container():
        st.header("🤖 Análise da IA")

        # <<< NOVO: A lógica de análise fica mais simples >>>
        if analyze_button and 'image_bytes' in st.session_state:
            # A variável 'question' já terá o valor correto (seja o digitado ou o padrão)
            try:
                with st.spinner("Analisando sua refeição... 🧑‍🍳"):
                    answer = process_image_and_question(st.session_state['image_bytes'], question)
                st.session_state['answer'] = answer
                logger.info("Análise concluída com sucesso.")

            except Exception as e:
                logger.exception("Erro ao processar a imagem no app.py")
                st.error(f"❌ Desculpe, ocorreu um erro. Detalhes: {e}")
                st.session_state['answer'] = None
        
        if 'answer' in st.session_state and st.session_state['answer']:
            st.markdown(st.session_state['answer'])
        else:
            st.info("Aguardando uma imagem e uma pergunta para iniciar a análise.")
            st.markdown("<div style='text-align: center; font-size: 4em; margin-top: 50px;'>🍽️</div>", unsafe_allow_html=True)
            st.markdown("<p>Seus resultados aparecerão aqui.</p>", unsafe_allow_html=True)