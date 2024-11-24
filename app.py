import os.path

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_navigation_bar.example import logo_path

image = Image.open('img/genetic-algorithm-svgrepo-com.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
pages = ["Home", "Project1", "Project2", "Project3"]

logo_path = os.path.join(os.path.dirname(__file__), "img", "genetic-algorithm-svgrepo-com.svg")
pages = [" ", 'Home', 'Project1', 'Project2', 'Project3']

page = st_navbar(pages, styles=styles, logo_path=logo_path, options=options)
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)"
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    }
}
page = st_navbar(pages, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()



