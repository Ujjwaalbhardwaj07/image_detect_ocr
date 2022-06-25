import streamlit as st
from PIL import Image
image = Image.open('Products.png')

st.image(image, caption='BS: BASF-Sustaniblity score')
