import pyttsx3
import PyPDF2
from pydub import AudioSegment
import os
import streamlit as st

st.write(""" # Ouvir meu PDF """)

file = st.file_uploader('Selecione o PDF', ['pdf'])

if file:
    pdf_reader = PyPDF2.PdfFileReader(file)

    num_pages = pdf_reader.numPages

    engine = pyttsx3.init()

    audios = []
    names = []
    for num in range(0, num_pages):
        page = pdf_reader.getPage(num)

        engine.save_to_file(page.extractText(), f"audios/audio{num}.mp3")

        engine.runAndWait()
        engine.runAndWait()
        engine.runAndWait()
        engine.runAndWait()
        
        names.append(f"audio{num}.mp3")
        #audios.append(AudioSegment.from_wav(f"audio{num}.wav"))

    st.write(names)

    #final_audio = sum(audios)
    #final_audio.export('audio_final.waw', format='wav')

    #AudioSegment.from_wav('audio_final.wav').export('audio_final.mp3', format="mp3")

    #for file in names:
    #    os.remove(file)

    #st.audio(open('audio_final.mp3', 'rb'))