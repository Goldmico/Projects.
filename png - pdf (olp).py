import streamlit as st
from PIL import Image
import io
import time
import random

finish = ""

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}      /* hides hamburger menu */
header {visibility: hidden;}         /* hides top header */
footer {visibility: hidden;}         /* hides "Made with Streamlit" */
</style>
"""

if "images" not in st.session_state:
    st.session_state.images = []

if "last_capture" not in st.session_state:
    st.session_state.last_capture = None

if "pdf" not in st.session_state:
    st.session_state.pdf = None

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("Made with 💗 using python")
st.markdown(
    "<div style='border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:10px;text-align:center;'>For Optimi use only | Not for profitable use</div>",
    unsafe_allow_html=True)


st.title("prezzcanner🖨️")
st.write("Scan directly to your device!")


pdf_bytes = io.BytesIO()

take_image = st.camera_input("")
if take_image:
    if st.session_state.last_capture != take_image:
        img = Image.open(take_image).convert("RGB")
        st.session_state.images.append(img)
        st.write("Photo Taken!")
        st.session_state.last_capture = take_image

clear_all = st.button("Clear all photos")
if clear_all:
    st.session_state.images = []
    st.session_state.pdf = None
    st.session_state.last_capture = None
    st.write("Images Cleared!")

# 👇 GALLERY
if st.session_state.images:
    cols = st.columns(3)

    for i, img in enumerate(st.session_state.images):
        cols[i % 3].image(img, use_container_width=True)

finish = st.button("Finish")

if finish:
    if len(st.session_state.images) == 0:
        st.warning("No photos taken!")
    else:
        pdf_bytes = io.BytesIO()

        st.session_state.images[0].save(
            pdf_bytes,
            format="PDF",
            save_all=True,
            append_images=st.session_state.images[1:]
        )

        st.session_state.pdf = pdf_bytes.getvalue()

        st.success("Images saved!")

# 👇 DOWNLOAD (FIXED)
if st.session_state.pdf is not None:
    st.download_button(
        label="Download PDF",
        data=st.session_state.pdf,
        file_name="prezz_converted.pdf",
        mime="application/pdf"
    )

st.link_button("The OLP", "https://optimi.learning.co.za")

st.write("")
st.markdown(
    "<div style='border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:10px;text-align:center;'>| By prezz | Dont steal | Not open source | </div>",
    unsafe_allow_html=True)
st.markdown("<div style='border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:10px;text-align:center;'>A Non-Profit Optimi-use-only version of CamScanner</div>", unsafe_allow_html=True)

