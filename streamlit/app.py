import streamlit as st
import web.img
from pages.prediction_page import prediction_home

import os
import re
import base64
from pathlib import Path

import streamlit as st

def markdown_images(markdown):
    # example image markdown:
    # ![Test image](images/test.png "Alternate text")
    images = re.findall(r'(!\[(?P<image_title>[^\]]+)\]\((?P<image_path>[^\)"\s]+)\s*([^\)]*)\))', markdown)
    return images


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path, img_alt):
    img_format = img_path.split(".")[-1]
    img_html = f'<img src="data:image/{img_format.lower()};base64,{img_to_bytes(img_path)}" alt="{img_alt}" style="max-width: 100%;">'

    return img_html


def markdown_insert_images(markdown):
    images = markdown_images(markdown)

    for image in images:
        image_markdown = image[0]
        image_alt = image[1]
        image_path = image[2]
        if os.path.exists(image_path):
            markdown = markdown.replace(image_markdown, img_to_html(image_path, image_alt))
    return markdown


def hide_sidebar_navigation():
    """
    Hides the sidebar navigation in the Streamlit app.

    This function adds a CSS style to hide the sidebar navigation in the Streamlit app.

    Parameters:
    None

    Returns:
    None
    """
    hide_style = """
        <style>
        /* Hide the sidebar title */
        div[data-testid="stSidebarNav"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)


def read_markdown_file(markdown_file):
    """
    Reads the content of a markdown file.

    Args:
        markdown_file (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.
    """
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()

    content = markdown_insert_images(content)

    return content


if __name__ == "__main__":
    PAGES = {
        "Introduction": "pages/intro.md",
        "Data Analysis": "pages/data_analysis.md",
        "Machine Learning": "pages/machine_learning.md",
        "LeNet": "pages/lenet.md",
        "Transfer Learning": "pages/transfer_learning.md",
        "Interpretability": "pages/interpretability.md",
        "Prediction": prediction_home,
        "Summary": "pages/summary.md",
        "Team": "pages/team.md",
    }

    # Setup page configuration
    st.set_page_config(
        page_title="Plant recognition apr24", layout="wide", page_icon="🍃"
    )

    # Apply the CSS to hide sidebar navigation
    hide_sidebar_navigation()

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Select a page:", list(PAGES.keys()), label_visibility="collapsed"
    )

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
