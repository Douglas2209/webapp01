# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('caneca.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("ValverdeSubli")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Catalogo de Produto")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Caneca Tema (dia dos Pais)")

menu = ["Catalogo_de_Vendas",
        "Endereço_Comercial",
        "Inserir_Figura"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "Catalogo_de_Vendas":       
    st.image(image01, width=400, caption='Imagem ilustrativa do produto')
    Texto01 = '<p style="font-family:tahoma; color:red; font-size: 25px;">R$ 29,99 acima de 10 unidades 27,99'
    st.markdown(Texto01, unsafe_allow_html=True)
    st.write("Catalogo de vendas")    
    col1, col2 = st.columns((1,1))
        
elif choice == "Endereço_Comercial":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
