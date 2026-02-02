import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# basic page setup
st.set_page_config(page_title="Nic du Plessis", layout="wide")

# force dark background (streamlit theme alone wasn't enough)
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
# centered intro text
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px;">
        <h1 style="color:#00ff41;">Nic du Plessis</h1>
        <p style="color:#00ff41; font-size: 18px;">
            Computer Science & Physics Undergraduate
        </p>
        <p style="color:#00ff41; max-width: 700px; margin: auto;">
            .
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# regenerate button
# --------------------------------------------------
if "rerun" not in st.session_state:
    st.session_state.rerun = True

if st.button("Regenerate animation"):
    st.session_state.rerun = True

plot_spot = st.empty()

# --------------------------------------------------
# matrix-style rain
# --------------------------------------------------
if st.session_state.rerun:

    # random starting positions
    num_lines = 200
    x_pos = np.random.rand(num_lines)
    y_pos = np.random.rand(num_lines)

    # each line falls at a slightly different speed
    speeds = np.random.uniform(0.01, 0.04, num_lines)

    # limit frames so streamlit doesn't get angry
    for _ in range(100):

        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        # move the rain down
        y_pos -= speeds
        y_pos[y_pos < 0] = 1

        # draw each streak
        for i in range(num_lines):
            ax.plot(
                [x_pos[i], x_pos[i]],
                [y_pos[i], y_pos[i] + 0.05],
                color="#00ff41",
                linewidth=2,
                alpha=0.7
            )

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        plot_spot.pyplot(fig, use_container_width=True)
        plt.close(fig)

        time.sleep(0.05)

    st.session_state.rerun = False

# --------------------------------------------------
# footer
# --------------------------------------------------
st.caption(
    ."
)
