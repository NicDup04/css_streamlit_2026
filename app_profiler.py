import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")

st.title("Nic du Plessis")
st.subheader("Computer Science & Physics Undergraduate")

st.write("""
Aspiring researcher interested in computational physics,
visualization, and how complex systems emerge from simple rules.
""")

placeholder = st.empty()

for step in range(30):
    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    
    x = np.random.rand(200)
    y = np.random.rand(200)
    
    ax.scatter(x, y, c="lime", s=10)
    ax.axis("off")

    placeholder.pyplot(fig)
    plt.close(fig)
    time.sleep(0.1)
