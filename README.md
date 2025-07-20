# Multimodal Assistant 🥗

**Assistente Nutricional Multimodal com IA**

NMultimodal Assistant é uma aplicação web inteligente construída com Streamlit e LangChain que utiliza o poder dos modelos de linguagem multimodais (como o GPT-4o da OpenAI) para analisar imagens de alimentos.

Basta tirar uma foto ou enviar uma imagem de um prato, fazer uma pergunta, e a IA fornecerá uma análise detalhada sobre calorias estimadas, ingredientes e informações nutricionais.

![Demo do Multimodal Assistant](https://iaplaybook.tech/images/posts/multimodal-assistant-demo.gif) 


## ✨ Funcionalidades Principais

-   **Análise por Imagem:** Envie um arquivo de imagem (`jpg`, `jpeg`, `png`) para análise.
-   **Captura com a Câmera:** Tire uma foto do seu prato em tempo real diretamente pela aplicação.
-   **Interface de Pergunta Flexível:** Faça perguntas abertas sobre a imagem.
-   **Pergunta Padrão Automática:** Se nenhuma pergunta for feita, uma análise completa padrão é solicitada para facilitar o uso.
-   **UI Moderna e Responsiva:** Interface limpa, organizada em colunas e esteticamente agradável.
-   **Backend Modular:** Arquitetura de software bem estruturada, separando a interface (UI), a lógica de orquestração (pipeline) e as estratégias de IA.


## 🛠️ Tecnologias Utilizadas

-   **Frontend:** [Streamlit](https://streamlit.io/)
-   **Backend:** [Python 3.9+](https://www.python.org/)
-   **Orquestração de IA:** [LangChain](https://www.langchain.com/)
-   **Modelo de IA:** [OpenAI GPT-4o](https://openai.com/index/hello-gpt-4o/) (ou outro modelo multimodal)
-   **Gerenciamento de Dependências:** `pip` e `requirements.txt`


## 📂 Estrutura do Projeto

A estrutura do projeto foi projetada para ser modular e escalável, seguindo princípios de separação de responsabilidades.

```
MULTIMODAL-ASSISTANT/
├── .venv/                   # Ambiente virtual
├── pipeline/
│   └── multimodal_pipeline.py # Orquestra o fluxo principal da análise
├── strategies/
│   ├── llms/                  # (Opcional) Para lógicas de texto puro
│   ├── prompts/
│   │   └── base_prompt.py     # Centraliza os prompts do sistema para a IA
│   └── vision/
│       └── openai_vision.py   # Implementa a chamada para a API de visão da OpenAI
├── utils/
│   ├── logger.py            # Configuração do logger
│   └── validators.py        # (Opcional) Para validações de dados
├── .env                     # Arquivo para suas chaves de API (NÃO versionar)
├── .gitignore               # Arquivos e pastas a serem ignorados pelo Git
├── app.py                   # Arquivo principal da interface Streamlit
├── config.py                # Carrega as configurações do .env
└── requirements.txt         # Lista de dependências do projeto
```


## ⚙️ Instalação e Configuração

Siga estes passos para configurar e executar o projeto em sua máquina local.

### 1. Pré-requisitos

-   Python 3.9 ou superior
-   Git

### 2. Clone o Repositório

```bash
git clone https://github.com/EstevesMarques/multimodal-assistant.git
cd multimodal-assistant
```

### 3. Crie e Ative um Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

-   **No Windows:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

-   **No macOS/Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 4. Instale as Dependências

Crie um arquivo `requirements.txt` com o seguinte conteúdo:

```txt
streamlit
langchain-openai
python-dotenv
pillow
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### 5. Configure suas Variáveis de Ambiente

Você precisará de uma chave de API da OpenAI.

a. Crie um arquivo chamado `.env` na raiz do projeto.

b. Adicione sua chave de API a este arquivo:

```
# .env
OPENAI_API_KEY=sk-proj-......
OPENAI_LLM_MODEL=gpt-4o-mini-2024-07-18
OPENAI_COMPLETION_URL=https://api.openai.com/v1/chat/completions
OPENAI_TEMPERATURE=0.1
```

*O arquivo `.gitignore` já está configurado para ignorar o `.env`, garantindo que sua chave não seja enviada para o repositório.*


## 🚀 Como Executar

Com o ambiente virtual ativado e as dependências instaladas, inicie a aplicação Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente em seu navegador padrão no endereço `http://localhost:8501`.


## 🧠 Como Funciona o Fluxo de Análise

1.  **Interface (`app.py`):** O usuário envia uma imagem (upload ou câmera) e digita uma pergunta (ou deixa em branco para a pergunta padrão).
2.  **Acionamento:** Ao clicar em "Analisar", o `app.py` chama a função `process_image_and_question` do nosso pipeline.
3.  **Pipeline (`multimodal_pipeline.py`):** Esta camada atua como um orquestrador. Ela recebe os dados brutos, valida-os e direciona para a estratégia de visão correta.
4.  **Estratégia de Visão (`openai_vision.py`):**
    -   A imagem (em bytes) é codificada para o formato base64.
    -   O prompt do sistema (de `base_prompt.py`) é recuperado para dar instruções à IA.
    -   Usando LangChain, uma mensagem multimodal é montada, contendo as instruções, a pergunta do usuário e a imagem.
    -   Uma chamada é feita para a API da OpenAI.
5.  **Retorno:** A resposta em texto/markdown gerada pela IA flui de volta pelo mesmo caminho até ser exibida de forma elegante na interface do `app.py`.


## 🔮 Possíveis Melhorias Futuras

-   [ ] **Histórico de Análises:** Salvar as análises do usuário em um banco de dados local (SQLite) ou na nuvem.
-   [ ] **Suporte a Múltiplos Modelos:** Adicionar uma opção para escolher entre diferentes modelos de IA (ex: Google Gemini).
-   [ ] **Dashboard Nutricional:** Criar gráficos e visualizações para acompanhar a ingestão de nutrientes ao longo do tempo.
-   [ ] **Autenticação de Usuário:** Implementar um sistema de login para que cada usuário tenha seu próprio histórico.

---

## 📄 Licença

Este projeto está distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.