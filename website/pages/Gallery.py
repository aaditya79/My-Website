from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aaditya Pai's Portfolio", page_icon=":computer:", layout="wide") 

with st.container():
    left, right = st.columns(2)


    with left:
        st.header("Gallery :camera:")
        image1 = Image.open('IMG_2093.jpg')
        st.image(image1, width=450, caption="Donating 2,000+ facemasks") 
        image4 = Image.open('IMG_2094.jpg')
        st.image(image4, width=450, caption="Our efforts on the local newspaper") 
        image5 = Image.open('IMG_2096.jpg')
        st.image(image5, width=450, caption="Fundraising through 'Masala Night'") 

    
    with right:
        st.write("#")
        st.write("#")
        image2 = Image.open('IMG_2091.jpg')
        st.image(image2, width=400, caption="Constructing new classroom in primary school") 

        image3 = Image.open('IMG_2092.jpg')
        st.image(image3, width=400, caption="Inside constructed primary school classroom") 