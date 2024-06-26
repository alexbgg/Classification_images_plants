import streamlit as st
import web.img
from pages.prediction_page import prediction_home


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
