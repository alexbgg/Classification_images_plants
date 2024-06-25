from importlib import reload

from pages import intro, data_analysis, machine_learning, lenet, transfer_learning, interpretability, model, summary, team
import streamlit as st

reload(intro)
reload(data_analysis)
reload(machine_learning)
reload(lenet)
reload(transfer_learning)
reload(interpretability)
reload(model)
reload(summary)
reload(team)


PAGES = {
    "Intro": intro,
    "Data Analysis": data_analysis,
    "Machine Learning": machine_learning,
    "LeNet": lenet,
    "Transfer Learning": transfer_learning,
    "Interpretability": interpretability,
    "Prediction": model,
    "Summary": summary,
    "Team": team,
}


if __name__ == "__main__":
    st.set_page_config(page_title="Leukopy", page_icon="🩸")

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.write()
    # with st.spinner(f"Loading {selection} ..."):
    #     ast.shared.components.write_page(page)
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by the leukopy team. You can learn more about me at
        [leukopy](https://github.com/DataScientest/Leukopy).
        """
    )
