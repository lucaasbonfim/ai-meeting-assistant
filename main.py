# ===============================
# AI MEETING ASSISTANT
# Whisper (Transcrição local) + Gemini (Resumo Inteligente) + PDF
# ===============================

import streamlit as st
import tempfile
import os
from moviepy import VideoFileClip
import whisper
from fpdf import FPDF
import google.generativeai as genai
from dotenv import load_dotenv

# ===============================
# CONFIGURAÇÃO VIA .ENV
# ===============================
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada no arquivo .env")

genai.configure(api_key=GEMINI_API_KEY)

modelo_gemini = genai.GenerativeModel("models/gemini-flash-latest")

# ===============================
# CARREGAR MODELO WHISPER
# ===============================

@st.cache_resource
def carregar_whisper():
    return whisper.load_model("base")

model_whisper = carregar_whisper()

# ===============================
# FUNÇÕES DE PROCESSAMENTO
# ===============================

def extrair_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path + "_audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path


def transcrever_audio(audio_path):
    resultado = model_whisper.transcribe(audio_path, language="pt")
    return resultado["text"]


def gerar_resumo_gemini(texto):
    prompt = f"""
Você é um assistente especialista em documentação de reuniões.

Tarefa:
Gerar uma ATA PROFISSIONAL baseada na transcrição abaixo.

Siga obrigatoriamente este formato:

RESUMO:
(parágrafo claro, objetivo e profissional)

DECISÕES:
- decisão 1
- decisão 2

Caso não haja decisões claras, escreva:
- Nenhuma decisão formal foi registrada

Texto da reunião:
{texto}
"""

    resposta = modelo_gemini.generate_content(prompt)
    return resposta.text


def gerar_pdf(conteudo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    for linha in conteudo.split("\n"):
        pdf.multi_cell(0, 8, linha)

    caminho_pdf = tempfile.mktemp(suffix=".pdf")
    pdf.output(caminho_pdf)
    return caminho_pdf

# ===============================
# INTERFACE STREAMLIT
# ===============================

st.set_page_config(page_title="AI Meeting Assistant", page_icon="🧠")

st.title("🧠 AI Meeting Assistant")
st.markdown("### Envie o vídeo e gere automaticamente a ata profissional da reunião")

arquivo_video = st.file_uploader(
    "📹 Envie o vídeo da reunião",
    type=["mp4", "avi", "mov"]
)

if arquivo_video:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(arquivo_video.read())
        caminho_video = temp_video.name

    st.info("🎧 Extraindo áudio do vídeo...")
    audio = extrair_audio(caminho_video)

    st.info("📝 Transcrevendo reunião com Whisper...")
    transcricao = transcrever_audio(audio)

    st.subheader("📝 Transcrição gerada pela IA")
    st.text_area("Texto reconhecido:", transcricao, height=250)

    st.info("🧠 Gerando ATA com Gemini...")
    ata = gerar_resumo_gemini(transcricao)

    st.subheader("📄 ATA GERADA AUTOMATICAMENTE")
    st.markdown(ata)

    pdf_gerado = gerar_pdf(ata)

    with open(pdf_gerado, "rb") as f:
        st.download_button(
            label="📥 Baixar PDF da Ata",
            data=f,
            file_name="ata_reuniao.pdf",
            mime="application/pdf"
        )
