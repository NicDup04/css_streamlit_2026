import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="Profile | Astronomy", layout="wide")

# --------------------------------------------------
# Force dark theme
# --------------------------------------------------
st.markdown(
    """
    <style>
    body { background-color: black; }
    .stApp { background-color: black; }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("<h1 style='color:#00ff41;'>Nic du Plessis</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff41;'>Computer Science & Physics Undergraduate</p>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#00ff41; max-width: 800px;'>"
    "This interactive profile uses generative visuals to explore digital rain and "
    "the emergence of structure from randomness. The animation below gradually "
    "forms the word <b>ASTRONOMY</b>."
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")

placeholder = st.empty()

# --------------------------------------------------
# Matrix rain setup
# --------------------------------------------------
num_rain = 200
x_rain = np.random.rand(num_rain)
y_rain = np.random.rand(num_rain)

# --------------------------------------------------
# Generate letter points for 'ASTRONOMY'
# --------------------------------------------------
text = "ASTRONOMY"
font_size = 75  # safe size for Streamlit Cloud

fig_tmp, ax_tmp = plt.subplots(figsize=(8, 4))
ax_tmp.text(0.5, 0.5, text, fontsize=font_size, ha="center", va="center")
ax_tmp.set_xlim(0, 1)
ax_tmp.set_ylim(0, 1)
ax_tmp.axis("off")
fig_tmp.canvas.draw()

renderer = fig_tmp.canvas.get_renderer()
bbox = ax_tmp.texts[0].get_window_extent(renderer=renderer)

# Normalize bounding box
x0 = bbox.x0 / fig_tmp.bbox.width
y0 = bbox.y0 / fig_tmp.bbox.height
x1 = bbox.x1 / fig_tmp.bbox.width
y1 = bbox.y1 / fig_tmp.bbox.height

# Sample points inside the text bounding box
num_letter_points = 600
letter_x = np.random.uniform(x0, x1, num_letter_points)
letter_y = np.random.uniform(y0, y1, num_letter_points)

plt.close(fig_tmp)

# Letter opacity (fade-in control)
letter_alpha = np.zeros(num_letter_points)

# --------------------------------------------------
# Animation loop (completion-based, not frame-based)
# --------------------------------------------------
fade_speed = 0.015

while np.max(letter_alpha) < 1.0:
    fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")
    ax.set_facecolor("black")

    # Vertical matrix rain streaks
    for i in range(num_rain):
        y_rain[i] -= 0.035
        if y_rain[i] < 0:
            y_rain[i] = 1

        ax.plot(
            [x_rain[i], x_rain[i]],
            [y_rain[i], y_rain[i] + 0.06],
            color="#00ff41",
            alpha=0.6,
            linewidth=2
        )

    # Fade in letters
    letter_alpha += fade_speed
    letter_alpha = np.clip(letter_alpha, 0, 1)

    ax.scatter(
        letter_x,
        letter_y,
        c="#00ff41",
        s=14,
        alpha=letter_alpha
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    placeholder.pyplot(fig, use_container_width=True)
    plt.close(fig)
    time.sleep(0.08)

# --------------------------------------------------
# Final static state (clean finish)
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")
ax.set_facecolor("black")

ax.scatter(letter_x, letter_y, c="#00ff41", s=14)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

placeholder.pyplot(fig, use_container_width=True)
plt.close(fig)

st.caption(
    "Matrix-style generative visualization where digital rain converges to form the word "
    "'ASTRONOMY'. Built using Python, NumPy, Matplotlib, and Streamlit."
)
