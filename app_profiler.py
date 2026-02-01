import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Profile", layout="wide")

# Dark theme CSS
st.markdown("""
<style>
body { background-color: black; }
.stApp { background-color: black; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='color:#00ff41;'>Nic du Plessis</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff41;'>Computer Science & Physics Undergraduate</p>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff41; max-width: 800px;'>This interactive profile explores generative visuals, combining digital rain and stars to create a finite animation.</p>", unsafe_allow_html=True)

st.markdown("---")

placeholder = st.empty()

# Parameters
num_dots = 400  # falling rain
num_stars = 50  # fixed stars
width, height = 1, 1  # normalized axes

# Random initial positions for rain
x = np.random.rand(num_dots)
y = np.random.rand(num_dots)

# Random positions for stars
star_x = np.random.rand(num_stars)
star_y = np.random.rand(num_stars)
stars_revealed = np.zeros(num_stars, dtype=bool)

# Animation loop
for frame in range(50):
    fig, ax = plt.subplots(figsize=(10,5), facecolor="black")
    ax.set_facecolor("black")

    # Scatter falling rain
    ax.scatter(x, y, c="#00ff41", s=6, alpha=0.5)

    # Update rain positions
    y = (y - 0.03) % 1
    x = (x + np.random.normal(0, 0.01, size=x.shape)) % 1

    # Gradually reveal stars
    if frame < num_stars:
        stars_revealed[frame] = True

    ax.scatter(star_x[stars_revealed], star_y[stars_revealed], c="white", s=15)

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis("off")

    placeholder.pyplot(fig, use_container_width=True)
    plt.close(fig)
    time.sleep(0.1)

st.caption("Matrix-style generative visualization with stars forming a constellation. ✨")
