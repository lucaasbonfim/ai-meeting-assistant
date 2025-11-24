# 🧠 AI MEETING ASSISTANT

Sistema inteligente para **geração automática de atas de reunião** a partir de vídeos, utilizando:

- 🎤 Whisper (transcrição local)
- 🧠 Gemini (resumo inteligente via IA)
- 📄 Geração de PDF
- 🌐 Interface web com Streamlit

---

## 🚀 Visão Geral

O **AI Meeting Assistant** é um projeto que automatiza todo o processo de documentação de reuniões, eliminando a necessidade de digitação manual de atas.

Fluxo completo do sistema:

1. O usuário envia um vídeo da reunião
2. O sistema extrai o áudio automaticamente
3. O Whisper converte o áudio em texto
4. O Gemini gera uma ata profissional
5. O sistema disponibiliza a ata em formato PDF

Tudo isso acontece de forma automática e inteligente.

---

## 🧩 Tecnologias Utilizadas

| Tecnologia       | Função                               |
| ---------------- | ------------------------------------ |
| Streamlit        | Interface web interativa             |
| Whisper (OpenAI) | Transcrição de áudio local           |
| Gemini API       | Resumo inteligente e decisões        |
| MoviePy          | Extração de áudio do vídeo           |
| FPDF             | Geração do PDF                       |
| Python-dotenv    | Gerenciamento seguro das credenciais |

---

## 📁 Estrutura do Projeto

```
ai-meeting-assistant/
│
├── main.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## 🔧 Configuração do Ambiente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/ai-meeting-assistant.git
cd ai-meeting-assistant
```

### 2️⃣ Crie o arquivo .env

Na raiz do projeto, crie um arquivo chamado `.env`:

```
GEMINI_API_KEY=SUA_CHAVE_DO_GOOGLE_AI_STUDIO
```

⚠️ A chave deve ser gerada em: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 📦 Instalação das Dependências

Crie o arquivo `requirements.txt` com o seguinte conteúdo:

```
streamlit
whisper
openai-whisper
moviepy
fpdf
google-generativeai
python-dotenv
torch
numpy
```

Instale tudo com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

Para iniciar o sistema, execute o comando abaixo:

```bash
python -m streamlit run main.py
```

Depois, abra no navegador:

```
http://localhost:8501
```

---

## 🛠 Como Usar

1. Faça upload de um vídeo da reunião
2. Aguarde a transcrição automática
3. A IA gera a ata profissional
4. Clique em **Baixar PDF da Ata**

---

## 📝 Exemplo de Ata Gerada

```
RESUMO:
A reunião teve como foco a definição de responsabilidades dos participantes, distribuindo tarefas específicas para as áreas de desenvolvimento do projeto.

DECISÕES:
- Hugo ficou responsável pelos modelos agendados.
- Leano ficou responsável pelo front-end utilizando Figma e React.
```

---

## 🔒 Segurança

- As chaves da API nunca são versionadas
- O sistema utiliza `.env` para proteger credenciais
- O arquivo `.env` deve estar listado no `.gitignore`

---

## 📌 Possíveis Melhorias Futuras

- Área de login e autenticação
- Histórico de reuniões
- Dashboard de atas
- Geração de DOCX
- Exportação automática por e-mail
- Sistema de versionamento de atas

---

## 👨‍💻 Autor

Desenvolvido por **Lucas Cardoso Bonfim**

Projeto acadêmico e experimental com foco em Inteligência Artificial aplicada à automação de processos administrativos.

---

## ✅ Status do Projeto

🟢 Em funcionamento
