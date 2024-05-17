import streamlit as st
from keras.models import load_model
from PIL import Image
from streamlit_option_menu import option_menu
from util import classify
import base64


original_title = '<b><center><p style="font-size: 60px; border-radius:50px; color:black; background-color: #B5C0D0;">Pneumonia detection</p></center></b>'
st.markdown(original_title, unsafe_allow_html=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:bgs/background.jfif;base64,%s");
    background-position: center;
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('bgs/background.jfif')
selected = option_menu(
            menu_title=None, 
            options=["HOME","VERIFY"],  
            orientation="horizontal",
        )
def app():    
    original_title = '<b><center><p style="font-family:Times new roman; color:black; font-size: 40px;">INTRODUCTION</p></center></b>'
    st.markdown(original_title, unsafe_allow_html=True)
    content_1 = '<p style="font-family:Times new roman; color:black; font-size: 20px; text-align: justify">Pneumonia is a respiratory infection that affects the lungs. It can be caused by various microorganisms, including bacteria, viruses, and fungi. The infection leads to inflammation in the air sacs of the lungs, causing them to fill with pus or other liquid, which can make breathing difficult.</p>'
    st.markdown(content_1, unsafe_allow_html=True)
    # Symptoms
    symptoms = [
        "Cough: Often producing phlegm.",
        "Fever: High body temperature is a common symptom.",
        "Shortness of Breath: Difficulty breathing or rapid breathing.",
        "Chest Pain: Pain or discomfort in the chest.",
        "Fatigue: Feeling excessively tired or weak.",
        "Confusion: Particularly in older adults."
    ]
    
    # Display symptoms using styled HTML
    styled_symptoms = [
        f'<li style="font-family: Times New Roman; color: black;font-size: 20px ;text-align: left;">{symptom}</li>'
        for symptom in symptoms
    ]
    
    st.markdown("<h2 style='font-family: Times New Roman; color: black; font-size: 20px;text-align: center;'>Symptoms:</h2>", unsafe_allow_html=True)
    st.markdown("<ul>" + "".join(styled_symptoms) + "</ul>", unsafe_allow_html=True)

def VERIFY():  
    st.header('Please upload a chest X-ray image')
    
    # upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])
    
    # load classifier
    model = load_model('./model/pneumonia_classifier.h5')
    
    # load class names
    with open('./model/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
        f.close()
    
    # display image
    if file is not None:
        image = Image.open(file).convert('RGB')
        st.image(image, use_column_width=True)
    
        # classify image
        class_name, conf_score = classify(image, model, class_names)
    
        # write classification
        st.write("## {}".format(class_name))
        st.write("### score: {}%".format(int(conf_score * 1000) / 10))

def FUTURE():    
    original_title = '<b><center><p style="font-family:Times new roman; color:White; font-size: 40px;">ABSTRACT</p></center></b>'
    st.markdown(original_title, unsafe_allow_html=True)
    content_1 = '<p style="font-family:Times new roman; color:White; font-size: 20px; text-align: justify">Pneumonia is a respiratory infection that affects the lungs. It can be caused by various microorganisms, including bacteria, viruses, and fungi. The infection leads to inflammation in the air sacs of the lungs, causing them to fill with pus or other liquid, which can make breathing difficult.</p>'
    st.markdown(content_1, unsafe_allow_html=True)
# set header
def main():

    if selected == 'HOME':
        app()
    elif selected == 'VERIFY':
        VERIFY()
    elif selected == 'FUTURE SCOPE':
        FUTURE()

if __name__ == "__main__":
    main()
