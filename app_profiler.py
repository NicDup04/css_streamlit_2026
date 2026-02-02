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
# Centered header content
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px;">
        <h1 style="color:#00ff41; font-size: 56px; margin-bottom: 10px;">
            Nicoleen du Plessis
        </h1>
        <h3 style="color:#00ff41; font-weight: normal; margin-top: 0;">
            Computer Science & Physics Undergraduate
        </h3>
        <p style="color:#00ff41; max-width: 800px; margin: 20px auto;">
            A simple generative visualization inspired by the Matrix.
            This project explores animation, randomness, and visual effects
            using Python and Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# Regenerate button logic
# --------------------------------------------------
if "regen" not in st.session_state:
    st.session_state.regen = True

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔁 Regenerate rain"):
        st.session_state.regen = True

placeholder = st.empty()

# --------------------------------------------------
# Matrix rain animation
# --------------------------------------------------
def matrix_rain():
    np.random.seed()

    n_drops = 250
    x = np.random.rand(n_drops)
    y = np.random.rand(n_drops)
    speed = np.random.uniform(0.01, 0.05, n_drops)

    frames = 120

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
