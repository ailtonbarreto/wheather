#App clima

import streamlit as st
import requests as rq
from datetime import datetime
from datetime import time

#--------------------------------------------------------------------------------
#Configuracao pagina

st.set_page_config(page_title="App clima",layout='centered',page_icon='🌥')

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)


container = st.container()

#--------------------------------------------------------------------------------
#chave api

apikey = 'd66a70f6c2960de613aae17abe518df9'

#--------------------------------------------------------------------------------
#seletor cidade
with container:
    cidade = st.text_input('Cidade').upper()


#--------------------------------------------------------------------------------
#link api

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={apikey}&lang=pt_br"

#--------------------------------------------------------------------------------
#requisicao

requisicao = rq.get(link)

#--------------------------------------------------------------------------------
#dados

hora = datetime.now().time()

noite = time(hour=18, minute=00, second=00)

requsicao_dic = requisicao.json()

#--------------------------------------------------------------------------------


try:
    descricao = requsicao_dic['weather'][0]['description']
    temperatura = requsicao_dic['main']['temp'] - 273.15
    icon = requsicao_dic['weather']['icon']
except KeyError:
    descricao = "Cidade não encontrada"
    temperatura = "0"

#--------------------------------------------------------------------------------
#layout

temp = f'{int(temperatura)}°C'

with container:
    st.write(descricao)


#--------------------------------------------------------------------------------
    
desativardetalhes = """
    <style>
    [data-testid="StyledFullScreenButton"]
    {
    visibility: hidden;
    }
    </style>
"""
st.markdown(desativardetalhes,unsafe_allow_html=True)

containerborda = """
    <style>
    [data-testid="stVerticalBlockBorderWrapper"]
    {
    border-radius: 18px;
    background-color: black;
    padding: 30px;
    opacity: 70%;
    text-align: center;
    }
    </style>
"""
st.markdown(containerborda,unsafe_allow_html=True)


    

