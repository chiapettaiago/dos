import streamlit as st
import pandas as pd

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Organização de Estoque")
df = pd.read_excel("exemplo.xlsx")
st.sidebar.title("Opções do App")
section = st.sidebar.selectbox("Funções", ["Selecionar...", "Organização de Estoque"])

#Módulo de Consulta
if section == "Organização de Estoque":
    seletor = st.slider("Procure por ID ou Código", 0, 26)
    if seletor == 0:
        numero = df.query('ID == 0')
        st.table(numero)
    elif seletor == 1:
        numero = df.query('ID == 1')
        st.table(numero)
    elif seletor == 2:
        numero = df.query('ID == 2')
        st.table(numero)
    elif seletor == 3:
        numero = df.query('ID == 3')
        st.table(numero)
    elif seletor == 4:
        numero = df.query('ID == 4')
        st.table(numero)
    elif seletor == 5:
        numero = df.query('ID == 5')
        st.table(numero)
    elif seletor == 6:
        numero = df.query('ID == 6')
        st.table(numero)
    elif seletor == 7:
        numero = df.query('ID == 7')
        st.table(numero)
    elif seletor == 8:
        numero = df.query('ID == 8')
        st.table(numero)
    elif seletor == 9:
        numero = df.query('ID == 9')
        st.table(numero)
    elif seletor == 10:
        numero = df.query('ID == 10')
        st.table(numero)
    elif seletor == 11:
        numero = df.query('ID == 11')
        st.table(numero)
    elif seletor == 12:
        numero = df.query('ID == 12')
        st.table(numero)
    elif seletor == 13:
        numero = df.query('ID == 13')
        st.table(numero)
    elif seletor == 14:
        numero = df.query('ID == 14')
        st.table(numero)
    elif seletor == 15:
        numero = df.query('ID == 15')
        st.table(numero)
    elif seletor == 16:
        numero = df.query('ID == 16')
        st.table(numero)
    elif seletor == 17:
        numero = df.query('ID == 17')
        st.table(numero)
    elif seletor == 18:
        numero = df.query('ID == 18')
        st.table(numero)
    elif seletor == 19:
        numero = df.query('ID == 19')
        st.table(numero)
    elif seletor == 20:
        numero = df.query('ID == 20')
        st.table(numero)
    elif seletor == 21:
        numero = df.query('ID == 21')
        st.table(numero)
    elif seletor == 22:
        numero = df.query('ID == 22')
        st.table(numero)
    elif seletor == 23:
        numero = df.query('ID == 23')
        st.table(numero)
    elif seletor == 24:
        numero = df.query('ID == 24')
        st.table(numero)
    elif seletor == 25:
        numero = df.query('ID == 25')
        st.table(numero)
    elif seletor == 26:
        numero = df.query('ID == 26')
        st.table(numero)