


# Importa las bibliotecas
from googletrans import Translator
from gtts import gTTS
import streamlit as st


# Título de la aplicación
st.title("Traductor y Texto a Voz")

# Introducción
st.write("""
Esta aplicación te permite traducir una frase a otro idioma y convertirla en audio.
Ingresa una frase y selecciona el idioma de destino para comenzar.
""")

# Solicita la frase y el idioma de destino
frase = st.text_input("Ingresa la frase que quieres traducir:")
idioma_destino = st.selectbox("Selecciona el idioma de destino:", ["es", "fr", "de", "ja", "zh", "ar"])



# Verifica si se ingresó una frase y un idioma de destino
if frase and idioma_destino:
    # Crea una instancia del traductor
    traductor = Translator()
    # Traduce la frase al idioma de destino
    traduccion = traductor.translate(frase, dest=idioma_destino)
    frase_traducida = traduccion.text

    # Imprime la frase traducida
    st.write("Frase traducida:", frase_traducida)

    # Crea una instancia de gTTS para generar el audio
    tts = gTTS(text=frase_traducida, lang=idioma_destino)

    # Guarda el archivo de audio en un directorio temporal
    temp_audio_file = "temp.mp3"
    tts.save(temp_audio_file)

    # Reproduce el archivo de audio
    st.audio(temp_audio_file, format="audio/mp3")

