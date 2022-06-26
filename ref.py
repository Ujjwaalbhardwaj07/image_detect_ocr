# Import the required Libraries
import streamlit as st
import pandas as pd
import requests
import easyocr as ocr  #OCR
from PIL import Image #Image Processing
import numpy as np #Image Processing
import json
import folium
import base64
import time
from streamlit_lottie import st_lottie



st.set_page_config(layout="wide")


# Functions for each of the pages
def home():
    # title
    st.title("Scan Your Product")

    # subtitle
    st.markdown("Would love to see if its BASF Product!")

    st.markdown("")

    # open camera
    # picture = st.camera_input("Take your Picture")

    # if picture:
    #    st.image(picture)
    # image uploader
    image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

    @st.cache
    def load_model():
        reader = ocr.Reader(['de'], model_storage_directory='.')
        return reader

    reader = load_model()  # load model

    if image is not None:

        input_image = Image.open(image)  # read image
        # st.image(input_image) #display image

        with st.spinner("Processing "):

            result = reader.readtext(np.array(input_image))

            result_text = []  # empty list for results

            for text in result:
                result_text.append(text[1])
                print(result_text)

            URL = "https://basfhackathon.herokuapp.com/ingredients/basf/ingredients"
            data_raw = ['Affinisphere C00465', 'Cegesoft HF 62', 'stearyl alcohol']
            data = json.dumps(result_text)
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.post(url=URL, data=data, headers=headers)
            st.markdown(response.text, unsafe_allow_html=True)
            st.write(result_text)
        # st.success("H

    else:
        st.write("Upload an Image")

    st.caption("Made by HerHackathon ❤️ by @ WeinTech")

def data_summary():
    st.header('sUSTAINABLITY INTELLIGENCE MATRICS')
    import time
     

    #lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_Z6rQ9X.json"
    # lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
    #lottie_hello = load_lottieurl(lottie_url_hello)
    # lottie_download = load_lottieurl(lottie_url_download)

    #st_lottie(lottie_hello, key="hello")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_Z6rQ9X.json"
    #lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello")
    #######################
    st.title(" Impact_we_Create")

    cities = pd.read_csv('country.csv')
    print(cities.shape)
    cities.head(3)

    world_all_cities_tooltip = folium.Map(
        zoom_start=5,
        location=[48.133932434766733, 9.103938729508073]
    )

    for _, city in cities.iterrows():
        folium.Marker(
            location=[city['latitude'], city['longitude']],
            popup=city['Sales'],

        ).add_to(world_all_cities_tooltip)

    world_all_cities_tooltip

    # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

    ""                                     ""
    ""                                     ""
    file_ = open(".\Product-Impact.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="demo gif">',
        unsafe_allow_html=True,
    )


def data_header():
    st.header('PRODUCT SUGGESTION')
    image = Image.open('Products.png')
    st.image(image, caption='BS: BASF-Sustaniblity score')





# Add a title and intro text
st.title('Everywhere BASF')

# Sidebar setup
st.sidebar.title('Sidebar')
# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Impact we create', 'Product_Suggestion'])


# Navigation options
if options == 'Home':
    home()
elif options == 'Impact we create':
    data_summary()
elif options == 'Product_Suggestion':
    data_header()