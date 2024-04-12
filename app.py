import pygame
import streamlit as st
from googletrans import LANGUAGES, Translator
import comprehension_check

translator = Translator()

def main(): 
    pygame.mixer.init()  # Initialize the mixer module.
    st.set_page_config(page_title='Multilingual Virtual Classroom Assistant', page_icon='📚')   # Set page title and icon
    page = st.sidebar.radio('Explore', ['Home', 'Comprehension Check', 'Text Language Translator', 'Voice Language Translator'])

    if page == 'Home':
        st.title('Welcome to the Multilingual Virtual Classroom Assistant!')
        st.write('Our app aims to revolutionize the way students learn by providing real-time translation services, comprehension checks, and accessibility features.')
        st.image('https://murf.ai/resources/media/posts/111/34370533_2203.q702.012.F.m005.c7.language-course-2.jpg', width=680, )
        st.write('Developed by Team TNcpl026 | 2024')

    elif page == 'Comprehension Check':
        comprehension_check.page_1()
        
# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))