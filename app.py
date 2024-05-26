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
except KeyError:
    descricao = "Cidade não encontrada"
    temperatura = "0"

st.write(link)
#--------------------------------------------------------------------------------
#layout

temp = f'{int(temperatura)}°C'

with container:
    if cidade == "":
        st.subheader("digite uma cidade",anchor=False)
    if descricao == "nublado":
        st.title(temp,anchor=False)
        st.image("nublado.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "chuva moderada":
        st.title(temp,anchor=False)
        st.image("chuva moderada.png",use_column_width=True)
        st.title(descricao,anchor=False) 
    if descricao == "ensolarado":
        st.title(temp,anchor=False)
        st.image("ensolarado.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "névoa":
        st.title(temp,anchor=False)
        st.image("nevoa.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "céu limpo" and hora >= noite:
        st.title(temp,anchor=False)
        st.image("lua céu claro.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "nuvens dispersas": 
        st.title(temp,anchor=False)
        st.image("nuvens dispersas.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "chuva leve": 
        st.title(temp,anchor=False)    
        st.image("chuva leve.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "céu limpo" and hora <= noite:
        st.title(temp,anchor=False)
        st.image("ensolarado.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "algumas nuvens" and hora <= noite:
        st.title(temp,anchor=False)
        st.image("poucas nuvens dia.png",use_column_width=True)
        st.title(descricao,anchor=False)
    if descricao == "algumas nuvens" and hora >= noite:
         st.title(temp,anchor=False)
         st.image("poucas nuvens noite.png",use_column_width=True)
         st.title(descricao,anchor=False)
    if descricao == "Cidade não encontrada" and cidade != "":
        st.image("not-found.png",use_column_width=True)
        st.subheader("Cidade não encontrada",anchor=False)
    

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


    

