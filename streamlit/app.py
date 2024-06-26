import utils
from pages.prediction_page import prediction_home

import streamlit as st

if __name__ == "__main__":
    PAGES = {
        "Introduction": "web/intro.md",
        "Data Analysis": "web/data_analysis.md",
        "Machine Learning": "web/machine_learning.md",
        "LeNet": "web/lenet.md",
        "Transfer Learning": "web/transfer_learning.md",
        "Interpretability": "web/interpretability.md",
        "Prediction": prediction_home,
        "Summary": "web/summary.md",
        "Team": "web/team.md",
    }

    # Setup page configuration
    st.set_page_config(page_title="Plant recognition apr24", layout="wide", page_icon="🍃")

    # Apply the CSS to hide sidebar navigation
    utils.hide_sidebar_navigation()

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Select a page:", options=list(PAGES.keys()), label_visibility="collapsed", key="nav_radio_box")

    # Render the content of the selected page
    page_content_or_func = PAGES[selection]

    # If it's a function, call it to render the page
    if callable(page_content_or_func):
        page_content_or_func()
    else:
        content = utils.read_markdown_file(page_content_or_func)
        st.markdown(content, unsafe_allow_html=True)

    st.sidebar.title("Team")
    st.sidebar.info(
        """
        This app is maintained by the Plant recognition team.
        For more information, visit our:
        
        [Plant Recognition Apr24 GitHub](https://github.com/DataScientest-Studio/apr24_bds_int_plant_recognition).
        """
    )
