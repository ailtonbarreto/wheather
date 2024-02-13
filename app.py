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


col1, col2, col3 = st.columns([1,5,1])
col4,col5,col6 = st.columns([1,5,1])
#--------------------------------------------------------------------------------
#chave api

apikey = 'd66a70f6c2960de613aae17abe518df9'

#--------------------------------------------------------------------------------
#seletor cidade
with col2:
    cidade = st.text_input('Cidade').upper()

# if cidade=="":
#     cidade = "Franca"
    

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


try:
    descricao = requsicao_dic['weather'][0]['description']
    temperatura = requsicao_dic['main']['temp'] - 273.15
except KeyError:
    descricao = "Cidade não encontrada"
    temperatura = "0"

# https://openweathermap.org/weather-conditions
#--------------------------------------------------------------------------------
#layout

temp = f'{int(temperatura)}°C'

with col5:
    st.title(temp,anchor=False)
    if descricao == "nublado":
        st.image("nublado.png",width=500)
    if descricao == "ensolarado":
        st.image("ensolarado.png",width=500)
    if descricao == "névoa":
        st.image("nevoa.png",width=500)
    if descricao == "céu limpo" and hora >= noite:
        st.image("lua céu claro.png",width=500)
    if descricao == "céu limpo" and hora <= noite:  
        st.image("ensolarado.png",width=500)
    if descricao == "algumas nuvens" and hora <= noite:
        st.image("sol com nuvens.png",width=500)
    if descricao == "algumas nuvens" and hora >= noite:
         st.image("lua com nuvens.png",width=500)
    if descricao == "Cidade não encontrada":
        st.image("not-found.png",width=500)
    st.title(descricao,anchor=False)


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
    background-color: #0F303A;
    opacity: 90%;
    }
    </style>
"""
st.markdown(containerborda,unsafe_allow_html=True)

imagem = """
    <style>
    [data-testid="stImage"]
    {
    opacity: 100%;
    }
    </style>
"""
st.markdown(imagem,unsafe_allow_html=True)
    
