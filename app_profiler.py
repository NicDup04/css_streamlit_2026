import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Profile", layout="wide")

# Force dark theme background
st.markdown(
    """
    <style>
    body {
        background-color: black;
    }
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 style='color:#00ff41;'>Nic du Plessis</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#00ff41;'>Computer Science & Physics Undergraduate</p>",
    unsafe_allow_html=True
)

st.markdown("---")

placeholder = st.empty()

num_points = 300
x = np.random.rand(num_points)
y = np.random.rand(num_points)

for frame in range(25):
    fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")
    ax.set_facecolor("black")

    ax.scatter(x, y, c="#00ff41", s=6)

    y = (y - 0.04) % 1
    x = (x + np.random.normal(0, 0.01, size=x.shape)) % 1

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    placeholder.pyplot(fig, use_container_width=True)
    plt.close(fig)

    time.sleep(0.15)

st.caption(
    "Generative visualization inspired by matrix-style digital rain."
)
