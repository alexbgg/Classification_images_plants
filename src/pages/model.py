import streamlit as st


def prediction():
    # Dropdown menu for selecting an option
    option = st.selectbox("Choose your favorite color:", ("Blue", "Green", "Red"))

    # Display text based on the user's selection
    if option == "Blue":
        st.write("You selected blue. Cool and calm!")
    elif option == "Green":
        st.write("You selected green. Fresh and bright!")
    elif option == "Red":
        st.write("You selected red. Bold and energetic!")
