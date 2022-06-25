import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import requests
import json
import webbrowser

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#title
st.title("Scan Your Product")

#subtitle
st.markdown("Would love to see if its BASF Product!")

st.markdown("")

#open camera
#picture = st.camera_input("Take your Picture")

#if picture:
#    st.image(picture)
#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['de'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    #st.image(input_image) #display image

    with st.spinner("Processing "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])
            print(result_text)
            


        URL = "https://basfhackathon.herokuapp.com/ingredients/basf/ingredients"
        data_raw = ['Affinisphere C00465', 'Cegesoft HF 62', 'stearyl alcohol']
        data = json.dumps(result_text)
        headers={
            'Content-type':'application/json',
            'Accept':'application/json'
        }
        response = requests.post(url=URL, data=data, headers=headers)
        st.markdown(response.text, unsafe_allow_html=True)
        st.write(result_text)
    #st.success("Here you go!")
    
else:
    st.write("Upload an Image")

st.caption("Made by HerHackathon ❤️ by @ WeinTech")





