import base64

import streamlit as st
import pandas as pd
import numpy as np
import time
import pathlib


def app():
    header_html1 = "<p style='text-align-last:center;font-size: 2rem'>Team 5 Project</p>"
    st.markdown(
        header_html1, unsafe_allow_html=True,
    )
    

    def img_to_bytes(img_path):
        img_bytes = pathlib.Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    header_html = "<img src='data:image/png width=10 height=10;base64,{}' class='img-fluid' style='height: 200px;display: block;margin-left: auto;margin-right: auto;width: auto'>".format(
        img_to_bytes("twitter.png")
    )
    st.markdown(
        header_html, unsafe_allow_html=True,
    )

    header_html2 = "<img src='data:image/png width=10 height=10;base64,{}' class='img-fluid' style='height: 100px;display: block;margin-left: auto;margin-right: auto;margin-top: 52px;margin-bottom:39px;width: auto;'>".format(
        img_to_bytes("alpha.png")
    )
    st.markdown(
        header_html2, unsafe_allow_html=True,
    )

    header_html3 = "<p style='text-align-last:center;font-size: 1rem;padding: 10px; border: 1px solid rgba(9, 171, 59, 0.2);background-color:rgba(9, 171, 59, 0.2)'>Adwait Sathe | Sachin | Vivek Kulkarni</p>"
    st.markdown(
        header_html3, unsafe_allow_html=True,
    )
    # st.button("Re-run")




