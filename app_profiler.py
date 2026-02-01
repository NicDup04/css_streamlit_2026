import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.write("Live version check")

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Nic du Plessis | Profile",
    layout="wide"
)

# --------------------------------------------------
# Matrix-style background
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
# Header text
# --------------------------------------------------
st.markdown(
    "<h1 style='color:#00ff41;'>Nic du Plessis</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color:#00ff41;'>Computer Science & Physics Undergraduate</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#00ff41; max-width: 800px;'>"
    "This interactive profile explores generative visuals as a way of presenting "
    "technical identity. While I am still an undergraduate, the project reflects my "
    "interests in computation, visualization, and the communication of complex ideas "
    "through code."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# Animation placeholder
# --------------------------------------------------
placeholder = st.empty()

# Initial random points
num_points = 350
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# --------------------------------------------------
# Matrix-style animation loop
# --------------------------------------------------
for frame in range(35):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor("black")

    # Scatter points
    ax.scatter(x, y, c="#00ff41", s=6, alpha=0.6)

    # Move points downward (matrix rain effect)
    y = (y - 0.03) % 1
    x = (x + np.random.normal(0, 0.005, size=x.shape)) % 1

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    placeholder.pyplot(fig, use_container_width=True)
    plt.close(fig)

    time.sleep(0.08)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption(
    "Generative visualization inspired by matrix-style digital rain. "
    "Built with Python, NumPy, Matplotlib, and Streamlit."
)

