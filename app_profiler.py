import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Nicoleen du Plessis"
field = "Astrophysics"
institution = "North-West University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Laser_Towards_Milky_Ways_Centre.jpg/1280px-Laser_Towards_Milky_Ways_Centre.jpg",
    caption="Wikipedia"
)

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"

st.write(f"You can reach {name} at {email}.")

