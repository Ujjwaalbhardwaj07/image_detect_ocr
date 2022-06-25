import streamlit as st
import folium
import pandas as pd
import base64

##################################
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_Z6rQ9X.json"
#lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
#lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello")


#######################
st.title(" OUR GLOBAL DISTRIBUTION")

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


#st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

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