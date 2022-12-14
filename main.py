import streamlit as st
import pandas as pd

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Coutt Modas")
df = pd.read_excel("exemplo.xlsx")
st.sidebar.title("Opções do App")
section = st.sidebar.selectbox("Funções", ["Selecionar...", "Organização de Estoque", "Inserir Produto", "Atualizar Produtos", "Deletar Produtos"])

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
if section == "Inserir Produto":
  st.text ("Insira aqui o Produto")
  resposta1 = st.text_input("Digite o Código ou nome do Produto")
  st.text ("Quantidade do Produto")
  resposta2 = st.text_input("Digite a Quantidade")
  st.text ("Digite o Preço do Produto")
  resposta3 = st.text_input("Digite o Valor")
if section == "Atualizar Produtos":
  st.text ("Digite o Código ou nome do Produto")
  resposta4 = st.text_input("Atualize o Código do Produto")
  st.text ("Digite a Quantidade do Produto")
  resposta5 = st.text_input("Atualize a quantidade")
  st.text ("Digite o Preço do Produto")
  resposta6 = ("Atualize o Valor do Produto")
if section == "Deletar Produtos":
  st.text ("Digite o Nome ou Código do Produto Vraus")
  resposta7 = ("Digite o Produto a ser Deletado")
  
about = st.sidebar.selectbox("Informações do sistema", ["Selecionar...", "Sobre o sistema", "Política de Privacidade", "Termos de uso"])
if about == "Sobre o sistema":
  st.header("Sistema DoS versão 0.34")
  st.text("Programador e CEO: Iago Chiapetta")
  st.text("Programador e Gerente de Qualidade de software: Patrick Gonçalves")
  st.text("Todos os direitos reservados")