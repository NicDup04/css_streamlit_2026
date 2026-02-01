import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Profile | Astronomy", layout="wide")

# -----------------------------
# Dark theme CSS
# -----------------------------
st.markdown("""
<style>
body { background-color: black; }
.stApp { background-color: black; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<h1 style='color:#00ff41;'>Nic du Plessis</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff41;'>Computer Science & Physics Undergraduate</p>", unsafe_allow_html=True)
st.markdown("<p style='color:#00ff41; max-width: 800px;'>Interactive visualization: Matrix-style digital rain gradually reveals the word 'ASTRONOMY'.</p>", unsafe_allow_html=True)
st.markdown("---")

placeholder = st.empty()

# -----------------------------
# Parameters
# -----------------------------
num_rain = 200           # number of vertical streaks
num_letters = 10         # resolution for letters fading
width, height = 1, 1

# Random rain positions
x_rain = np.random.rand(num_rain)
y_rain = np.random.rand(num_rain)

# Create letter coordinates for "ASTRONOMY"
text = "ASTRONOMY"
font_size = 150  # affects letter coverage
fig_temp, ax_temp = plt.subplots(figsize=(8,4))
ax_temp.text(0.5, 0.5, text, fontsize=font_size, ha='center', va='center')
ax_temp.set_xlim(0,1)
ax_temp.set_ylim(0,1)
ax_temp.axis('off')
fig_temp.canvas.draw()

# Extract bounding box and generate points
letters_positions = []
renderer = fig_temp.canvas.get_renderer()
for text_obj in ax_temp.texts:
    bbox = text_obj.get_window_extent(renderer=renderer)
    x0 = bbox.x0 / fig_temp.bbox.width
    y0 = bbox.y0 / fig_temp.bbox.height
    x1 = bbox.x1 / fig_temp.bbox.width
    y1 = bbox.y1 / fig_temp.bbox.height
    xs = np.random.uniform(x0, x1, 300)
    ys = np.random.uniform(y0, y1, 300)
    letters_positions.append((xs, ys))
plt.close(fig_temp)

# Flatten all points for letters
letter_x = np.concatenate([p[0] for p in letters_positions])
letter_y = np.concatenate([p[1] for p in letters_positions])
revealed_intensity = np.zeros(len(letter_x))  # 0=hidden, 1=full brightness

# -----------------------------
# Animation loop
# -----------------------------
frames = 80
for frame in range(frames):
    fig, ax = plt.subplots(figsize=(12,6), facecolor='black')
    ax.set_facecolor('black')

    # Vertical streaks for rain
    for i in range(num_rain):
        y_rain[i] -= 0.03
        if y_rain[i] < 0:
            y_rain[i] = 1
        ax.plot([x_rain[i], x_rain[i]], [y_rain[i], y_rain[i]+0.05], c="#00ff41", alpha=0.6, lw=2)

    # Gradually reveal letters
    fade_amount = 0.02  # how fast letters fade in
    revealed_intensity += fade_amount
    revealed_intensity = np.clip(revealed_intensity, 0, 1)
    ax.scatter(letter_x, letter_y, c="#00ff41", s=12, alpha=revealed_intensity)

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.axis('off')

    placeholder.pyplot(fig, use_container_width=True)
    plt.close(fig)
    time.sleep(0.08)

st.caption("Matrix-style digital rain forming the word 'ASTRONOMY'.")
