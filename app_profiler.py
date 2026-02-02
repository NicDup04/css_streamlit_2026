import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="Matrix Rain | Profile", layout="wide")

# --------------------------------------------------
# Dark background styling
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header content
# --------------------------------------------------
st.markdown("<h1 style='color:#00ff41;'>Nic du Plessis</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#00ff41;'>Computer Science & Physics Undergraduate</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color:#00ff41; max-width: 800px;'>"
    "A simple generative visualization inspired by the Matrix. "
    "This project explores animation, randomness, and visual effects "
    "using Python and Streamlit."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# Regenerate button logic
# --------------------------------------------------
if "regen" not in st.session_state:
    st.session_state.regen = True

if st.button("🔁 Regenerate rain"):
    st.session_state.regen = True

placeholder = st.empty()

# --------------------------------------------------
# Matrix rain animation
# --------------------------------------------------
def matrix_rain():
    np.random.seed()  # new randomness every run

    n_drops = 250
    x = np.random.rand(n_drops)
    y = np.random.rand(n_drops)
    speed = np.random.uniform(0.01, 0.05, n_drops)

    frames = 120  # finite, safe for Streamlit Cloud

    for _ in range(frames):
        fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")
        ax.set_facecolor("black")

        y -= speed
        y[y < 0] = 1

        for i in range(n_drops):
            ax.plot(
                [x[i], x[i]],
                [y[i], y[i] + 0.05],
                color="#00ff41",
                alpha=0.7,
                linewidth=2
            )

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        placeholder.pyplot(fig, use_container_width=True)
        plt.close(fig)
        time.sleep(0.05)

# --------------------------------------------------
# Run animation
# --------------------------------------------------
if st.session_state.regen:
    matrix_rain()
    st.session_state.regen = False

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption(
    "Matrix-style digital rain animation built with Python, NumPy, Matplotlib, and Streamlit."
)
