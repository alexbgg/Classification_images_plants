import os

from pages.model import prediction

import streamlit as st

def hide_sidebar_navigation():
    hide_style = """
        <style>
        /* Hide the sidebar title */
        div[data-testid="stSidebarNav"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)


# <div data-testid="stSidebarNav" class="st-emotion-cache-79elbk eczjsme17"><ul data-testid="stSidebarNavItems" class="st-emotion-cache-n8e7in eczjsme16"><li><div class="st-emotion-cache-j7qwjs eczjsme15"><a data-testid="stSidebarNavLink" href="http://localhost:8501/mp_app" class="st-emotion-cache-cw0gvd eczjsme14"><span class="st-emotion-cache-1dj0hjr eczjsme13">mp app</span></a></div></li><li><div class="st-emotion-cache-j7qwjs eczjsme15"><a data-testid="stSidebarNavLink" href="http://localhost:8501/page_4" class="st-emotion-cache-i45v5m eczjsme14"><span class="st-emotion-cache-1q2d4ya eczjsme13">page 4</span></a></div></li></ul><div data-testid="stSidebarNavSeparator" class="st-emotion-cache-1tuwfdi eczjsme0"></div></div>


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Function to read markdown files
def read_markdown_file(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()
    return content


PAGES = {
    "Introduction": "pages/intro.md",
    "Data Analysis": "pages/data_analysis.md",
    "Machine Learning": "pages/machine_learning.md",
    "LeNet": "pages/lenet.md",
    "Transfer Learning": "pages/transfer_learning.md",
    "Interpretability": "pages/interpretability.md",
    "Prediction": prediction,
    "Summary": "pages/summary.md",
    "Team": "pages/team.md",
}

if __name__ == "__main__":
    # Setup page configuration
    st.set_page_config(page_title="Plant recognition apr24", layout="wide", page_icon="🩸")

    # Apply the CSS to hide sidebar navigation
    hide_sidebar_navigation()

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    # Render the content of the selected page
    page_content_or_func = PAGES[selection]
    
    # If it's a function, call it to render the page
    if callable(page_content_or_func):
        page_content_or_func()
    else:
        content = read_markdown_file(page_content_or_func)
        st.markdown(content, unsafe_allow_html=True)

    st.sidebar.title("Team")
    st.sidebar.info(
        """
        This app is maintained by the Plant recognition team.
        For more information, visit our:
        
        [Plant Recognition Apr24 GitHub](https://github.com/DataScientest-Studio/apr24_bds_int_plant_recognition).
        """
    )
